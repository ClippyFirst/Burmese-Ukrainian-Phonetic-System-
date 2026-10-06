import { ONSETS, VOWELS, SIGNS, MEDIALS, PRACTICAL, RULES } from "./generated/data.js";

const source=document.querySelector("#source");
const results=document.querySelector("#results");
const empty=document.querySelector("#empty");
const issues=document.querySelector("#issues");
const issueText=document.querySelector("#issue-text");
const count=document.querySelector("#count");
const uk=document.querySelector("#uk");
const ipa=document.querySelector("#ipa");
const syllables=document.querySelector("#syllables");
const ukStatus=document.querySelector("#uk-status");
const ipaStatus=document.querySelector("#ipa-status");
const live=document.querySelector("#live");

const KINZI="င်္";
const VIRAMA="္";
const ASAT="်";
const MEDIAL_CHARS=new Set(Object.keys(MEDIALS));
const VOWEL_CHARS=new Set(Object.keys(SIGNS));
const BASE=new Set(Object.keys(ONSETS));

function normalize(text){ return text.normalize("NFC"); }
function isMyanmar(ch){ const n=ch.codePointAt(0); return n>=0x1000 && n<=0x109f; }

function segment(text){
  const s=normalize(text), out=[]; let i=0;
  while(i<s.length){
    if(!isMyanmar(s[i])){ out.push({raw:s[i],nonMyanmar:true}); i++; continue; }
    const start=i; i++;
    while(i<s.length && isMyanmar(s[i])){
      const prev=s[i-1];
      const isNewBase=BASE.has(s[i]) && prev!==VIRAMA && s.slice(Math.max(start,i-3),i)!==KINZI;
      if(isNewBase) break;
      i++;
    }
    out.push({raw:s.slice(start,i),nonMyanmar:false});
  }
  return out;
}

function parseCluster(raw){
  const sy={raw,onset:null,kinzi:false,conjunct:[],medials:[],vowels:[],asat:false,status:"ESTABLISHED",ipa:null,uk:null,notes:[]};
  let i=0;
  if(raw.startsWith(KINZI)){ sy.kinzi=true; i=3; }
  if(i>=raw.length || !BASE.has(raw[i])){ sy.status="UNSUPPORTED"; sy.notes.push("Не вдалося визначити початкову приголосну."); return sy; }
  sy.onset=raw[i]; i++;
  while(i<raw.length && raw[i]===VIRAMA){
    if(i+1<raw.length && BASE.has(raw[i+1])){sy.conjunct.push(raw[i+1]);i+=2;} else {sy.status="UNCERTAIN";sy.notes.push("Неповна послідовність virama.");break;}
  }
  while(i<raw.length && MEDIAL_CHARS.has(raw[i])){sy.medials.push(raw[i]);i++;}
  while(i<raw.length && VOWEL_CHARS.has(raw[i])){sy.vowels.push(raw[i]);i++;}
  while(i<raw.length){
    if(raw[i]===ASAT){sy.asat=true;i++;continue;}
    if(raw[i]==="ံ" || raw[i]==="့" || raw[i]==="း"){sy.notes.push("Просодичний/ритмічний знак збережено як аналітичний маркер.");sy.status="ANALYSIS_DEPENDENT";i++;continue;}
    sy.status="UNCERTAIN";sy.notes.push("Нерозібраний знак "+raw[i]);i++;
  }
  sy.ipa=deriveIpa(sy);
  if(!sy.ipa) sy.status=sy.status==="ESTABLISHED"?"NOT_ESTABLISHED":sy.status;
  sy.uk=renderUkrainian(sy.ipa);
  return sy;
}

function deriveIpa(sy){
  const onset=ONSETS[sy.onset];
  if(!onset) return null;
  const parts=[onset.ipa];
  for(const m of sy.medials){
    const id=MEDIALS[m]?.id;
    const map={medial_ya:"j",medial_ra:"r",medial_wa:"w",medial_ha:"h"};
    if(map[id]) parts.push(map[id]); else return null;
  }
  if(!sy.vowels.length){
    return null;
  }
  for(const sign of sy.vowels){
    const id=SIGNS[sign]?.unicode_name;
    const map={"MYANMAR VOWEL SIGN E":"e","MYANMAR VOWEL SIGN I":"i","MYANMAR VOWEL SIGN II":"iː","MYANMAR VOWEL SIGN U":"u","MYANMAR VOWEL SIGN UU":"uː","MYANMAR VOWEL SIGN TALL AA":"a","MYANMAR VOWEL SIGN AA":"a","MYANMAR VOWEL SIGN AI":"ɛ","MYANMAR SIGN ANUSVARA":""};
    if(!(id in map)) return null;
    parts.push(map[id]);
  }
  if(sy.kinzi) parts.push("ŋ");
  return parts.join("");
}

function candidateFor(segment){
  const direct=PRACTICAL[segment]||PRACTICAL[segment==="θ"?"θ~ð":segment];
  if(!direct) return {text:"",status:"NOT_ESTABLISHED",reason:"Немає точного правила для цього IPA-сегмента."};
  const row=direct[0];
  return {text:row.ukrainian_candidate,status:(row.status||"UNKNOWN").toUpperCase(),reason:row.policy,ruleIds:(RULES[segment]||RULES[segment==="θ"?"θ~ð":segment]||[]).map(x=>x.rule_id)};
}

function renderUkrainian(ipaText){
  if(!ipaText) return {text:"",status:"NOT_ESTABLISHED",parts:[]};
  const units=ipaText.match(/tʰ|kʰ|pʰ|sʰ|dʰ|bʰ|θ|ð|ɲ|ŋ|ɯ|ɡ|ʔ|[a-zɛɪɔəː]/g)||[];
  const parts=[]; let status="ESTABLISHED";
  for(const u of units){
    const c=candidateFor(u); parts.push(c);
    if(c.status!=="PROPOSED" && c.status!=="ESTABLISHED" && c.status!=="WELL_SUPPORTED") status=c.status;
  }
  return {text:parts.map(x=>x.text).join(""),status,parts};
}

function convert(text){
  const segments=segment(text);
  const parsed=segments.map(s=>s.nonMyanmar?s:parseCluster(s.raw));
  const ipaText=parsed.map(s=>s.nonMyanmar?s.raw:(s.ipa||"?")).join(" ");
  const ukText=parsed.map(s=>s.nonMyanmar?s.raw:(s.uk?.text||"")).join("");
  const real=parsed.filter(s=>!s.nonMyanmar);
  const statuses=real.map(s=>s.status);
  const worst=statuses.includes("NOT_ESTABLISHED")?"NOT_ESTABLISHED":statuses.includes("UNCERTAIN")?"UNCERTAIN":statuses.includes("ANALYSIS_DEPENDENT")?"ANALYSIS_DEPENDENT":"ESTABLISHED";
  return {input:text,normalized:normalize(text),ipa:ipaText,uk:ukText,status:worst,segments:parsed};
}

function render(){
  const text=source.value;
  count.textContent=text.length+" символів";
  if(!text){empty.hidden=false;results.hidden=true;issues.hidden=true;return;}
  const r=convert(text);
  empty.hidden=true;results.hidden=false;
  uk.textContent=r.uk||"—"; ipa.textContent=r.ipa||"—";
  ukStatus.textContent="Статус: "+r.status;
  ipaStatus.textContent=r.segments.some(x=>!x.nonMyanmar && !x.ipa)?"Частину фонетичної структури не встановлено для цього вводу.":"Структурно розпізнані сегменти.";
  syllables.replaceChildren();
  r.segments.forEach((s,index)=>{
    const row=document.createElement("div");row.className="syllable";
    if(s.nonMyanmar){row.textContent=s.raw+" · не-Myanmar";syllables.append(row);return;}
    const head=document.createElement("strong");head.textContent=String(index+1).padStart(2,"0")+"  "+s.raw;
    const detail=document.createElement("span");detail.textContent=(s.ipa||"IPA не встановлено")+" → "+(s.uk?.text||"—")+" · "+s.status;
    row.append(head,detail);
    if(s.notes.length){const note=document.createElement("small");note.textContent=s.notes.join(" ");row.append(note);}
    syllables.append(row);
  });
  const problems=r.segments.filter(s=>!s.nonMyanmar && (!s.ipa || s.status==="UNCERTAIN" || s.status==="NOT_ESTABLISHED"));
  issues.hidden=problems.length===0;
  issueText.textContent=problems.length?("Для "+problems.length+" сегмент"+(problems.length===1?"а":"ів")+" результат потребує додаткового аналізу; сервіс не вигадує відсутню відповідність."):"";
  live.textContent="Конвертацію завершено. Статус: "+r.status;
}

source.addEventListener("input",render);
document.querySelector("#example").addEventListener("click",()=>{source.value="မြန်မာ";render();source.focus();});
document.querySelector("#clear").addEventListener("click",()=>{source.value="";render();source.focus();});
document.querySelectorAll("[data-copy]").forEach(btn=>btn.addEventListener("click",async()=>{
  const value=document.querySelector("#"+btn.dataset.copy).textContent;
  try{await navigator.clipboard.writeText(value);btn.textContent="Скопійовано";setTimeout(()=>btn.textContent="Копіювати",1200);}catch{btn.textContent="Не вдалося";}
}));
render();
