import { ONSETS, SIGNS, MEDIALS, PRACTICAL, RULES } from "./generated/data.js";

const source=document.querySelector("#source"), results=document.querySelector("#results"), empty=document.querySelector("#empty");
const issues=document.querySelector("#issues"), issueText=document.querySelector("#issue-text"), count=document.querySelector("#count");
const uk=document.querySelector("#uk"), ipa=document.querySelector("#ipa"), syllables=document.querySelector("#syllables");
const ukStatus=document.querySelector("#uk-status"), ipaStatus=document.querySelector("#ipa-status"), live=document.querySelector("#live");

const KINZI="င်္", VIRAMA="္", ASAT="်";
const MEDIAL_CHARS=new Set(Object.keys(MEDIALS)), VOWEL_CHARS=new Set(Object.keys(SIGNS)), BASE=new Set(Object.keys(ONSETS));

function normalize(text){return text.normalize("NFC");}
function isMyanmar(ch){const n=ch.codePointAt(0);return n>=0x1000&&n<=0x109f;}

function segment(text){
  const s=normalize(text),out=[];let i=0;
  while(i<s.length){
    if(!isMyanmar(s[i])){out.push({raw:s[i],nonMyanmar:true});i++;continue;}
    const start=i;i++;
    while(i<s.length&&isMyanmar(s[i])){
      const prev=s[i-1],isCodaBase=BASE.has(s[i])&&s[i+1]===ASAT;
      const isNewBase=BASE.has(s[i])&&!isCodaBase&&prev!==VIRAMA&&prev!==ASAT&&s.slice(Math.max(start,i-3),i)!==KINZI;
      if(isNewBase)break;i++;
    }
    out.push({raw:s.slice(start,i),nonMyanmar:false});
  }
  return out;
}

function parseCluster(raw){
  const sy={raw,onset:null,kinzi:false,conjunct:[],medials:[],vowels:[],asat:false,status:"ESTABLISHED",ipa:null,uk:null,notes:[]};
  let i=0;
  if(raw.startsWith(KINZI)){sy.kinzi=true;i=3;}
  if(i>=raw.length||!BASE.has(raw[i])){sy.status="UNSUPPORTED";sy.notes.push("Не вдалося визначити початкову приголосну.");return sy;}
  sy.onset=raw[i++];
  while(i<raw.length&&raw[i]===VIRAMA){
    if(i+1<raw.length&&BASE.has(raw[i+1])){sy.conjunct.push(raw[i+1]);i+=2;}
    else{sy.status="UNCERTAIN";sy.notes.push("Неповна послідовність virama.");break;}
  }
  while(i<raw.length&&MEDIAL_CHARS.has(raw[i]))sy.medials.push(raw[i++]);
  if(i+1<raw.length&&BASE.has(raw[i])&&raw[i+1]===ASAT){sy.coda=raw[i];i+=2;sy.asat=true;}
  while(i<raw.length&&VOWEL_CHARS.has(raw[i]))sy.vowels.push(raw[i++]);
  if(!sy.coda&&i+1<raw.length&&BASE.has(raw[i])&&raw[i+1]===ASAT){sy.coda=raw[i];i+=2;sy.asat=true;}
  while(i<raw.length){
    if(raw[i]===ASAT){sy.asat=true;i++;continue;}
    if(raw[i]==="ံ"||raw[i]==="့"||raw[i]==="း"){sy.notes.push("Просодичний/ритмічний знак збережено як аналітичний маркер.");sy.status="ANALYSIS_DEPENDENT";i++;continue;}
    sy.status="UNCERTAIN";sy.notes.push("Нерозібраний знак "+raw[i++]);
  }
  sy.ipa=deriveIpa(sy);if(!sy.ipa&&sy.status==="ESTABLISHED")sy.status="NOT_ESTABLISHED";sy.uk=renderUkrainian(sy.ipa);return sy;
}

function deriveIpa(sy){
  const onset=ONSETS[sy.onset];if(!onset)return null;let initial=onset.ipa;const parts=[];
  if(sy.kinzi)parts.push("ŋ");
  const ids=sy.medials.map(m=>MEDIALS[m]?.id).filter(Boolean);
  const has=key=>ids.includes(key);
  // Standard Burmese has contextual medial realizations: /k kʰ g/ + -y/-r
  // become palatal affricates, while /ŋ/ + -r merges toward /ɲ/.
  if(has("medial_ya")||has("medial_ra")){
    if(initial==="k") initial="tɕ";
    else if(initial==="kʰ") initial="tɕʰ";
    else if(initial==="ɡ") initial="dʑ";
    else if(initial==="ŋ"&&has("medial_ra")) initial="ɲ";
  }
  // Ha-to is primarily a voicing/devoicing marker on sonorants, not an /h/ onset.
  if(has("medial_ha")){
    const devoiced={m:"m̥",n:"n̥","ŋ":"ŋ̊","ɲ":"ɲ̥",l:"l̥",w:"ʍ"};
    if(initial==="j"||initial==="r") initial="ʃ";
    else if(devoiced[initial]) initial=devoiced[initial];
    else return null;
  }
  parts.push(initial);
  if(has("medial_wa"))parts.push("w");
  if(!sy.vowels.length){if(sy.coda||sy.asat)return null;parts.push("a");}
  const map={"MYANMAR VOWEL SIGN E":"e","MYANMAR VOWEL SIGN I":"i","MYANMAR VOWEL SIGN II":"iː","MYANMAR VOWEL SIGN U":"u","MYANMAR VOWEL SIGN UU":"uː","MYANMAR VOWEL SIGN TALL AA":"a","MYANMAR VOWEL SIGN AA":"a","MYANMAR VOWEL SIGN AI":"ɛ","MYANMAR SIGN ANUSVARA":""};
  for(const sign of sy.vowels){const id=SIGNS[sign]?.unicode_name;if(!(id in map))return null;parts.push(map[id]);}
  if(sy.coda)parts.push(ONSETS[sy.coda]?.ipa||"");return parts.join("");
}

function candidateFor(segment){
  const direct=PRACTICAL[segment]||PRACTICAL[segment==="θ"?"θ~ð":segment];
  if(!direct)return{text:"",status:"NOT_ESTABLISHED",reason:"Немає точного правила для цього IPA-сегмента."};
  const row=direct[0];
  return{text:row.ukrainian_candidate,status:(row.status||"UNKNOWN").toUpperCase(),reason:row.policy,ruleIds:(RULES[segment]||RULES["/"+segment+"/"]||[]).map(x=>x.rule_id)};
}

function renderUkrainian(ipaText){
  if(!ipaText)return{text:"",status:"NOT_ESTABLISHED",parts:[]};
  const units=ipaText.match(/tɕʰ|tɕ|dʑ|tʰ|kʰ|pʰ|sʰ|dʰ|bʰ|m̥|n̥|ŋ̊|ɲ̥|l̥|ʍ|ʃ|θ|ð|ɲ|ŋ|ɯ|ɡ|ʔ|[a-zɛɪɔəː]/g)||[];
  const parts=[];let status="ESTABLISHED";
  for(const u of units){const c=candidateFor(u);parts.push(c);if(!["PROPOSED","ESTABLISHED","WELL_SUPPORTED"].includes(c.status))status=c.status;}
  return{text:parts.map(x=>x.text).join(""),status,parts};
}

function convert(text){
  const normalized=normalize(text),parsed=segment(normalized).map(s=>s.nonMyanmar?s:parseCluster(s.raw)),myanmar=parsed.filter(s=>!s.nonMyanmar);
  const ipaText=parsed.map(s=>s.nonMyanmar?s.raw:(s.ipa||"?")).join(""),ukText=parsed.map(s=>s.nonMyanmar?s.raw:(s.uk?.text||"")).join("");
  const statuses=myanmar.map(s=>s.status),ukStatuses=myanmar.flatMap(s=>s.uk?.parts?.map(p=>p.status)||[]),all=[...statuses,...ukStatuses];
  let status;
  if(!myanmar.length)status="UNSUPPORTED";else if(all.includes("UNCERTAIN")||all.includes("UNSUPPORTED"))status="UNCERTAIN";
  else if(all.includes("NOT_ESTABLISHED"))status="NOT_ESTABLISHED";else if(all.includes("ANALYSIS_DEPENDENT"))status="ANALYSIS_DEPENDENT";
  else if(all.includes("PROPOSED"))status="PROPOSED";else status="ESTABLISHED";
  return{input:text,normalized,ipa:ipaText,uk:ukText,status,segments:parsed};
}

function render(){
  const text=source.value;count.textContent=text.length+" символів";
  if(!text){empty.hidden=false;results.hidden=true;issues.hidden=true;return;}
  const r=convert(text);empty.hidden=true;results.hidden=false;uk.textContent=r.uk||"—";ipa.textContent=r.ipa||"—";
  ukStatus.textContent="Статус: "+r.status;
  ipaStatus.textContent=r.segments.some(x=>!x.nonMyanmar&&!x.ipa)?"Частину фонетичної структури не встановлено для цього вводу.":"Структурно розпізнані сегменти.";
  syllables.replaceChildren();
  r.segments.forEach((s,index)=>{const row=document.createElement("div");row.className="syllable";
    if(s.nonMyanmar){row.textContent=s.raw+" · збережено без змін";syllables.append(row);return;}
    const head=document.createElement("strong");head.textContent=String(index+1).padStart(2,"0")+"  "+s.raw;
    const detail=document.createElement("span");detail.textContent=(s.ipa||"IPA не встановлено")+" → "+(s.uk?.text||"—")+" · "+s.status;row.append(head,detail);
    if(s.notes.length){const note=document.createElement("small");note.textContent=s.notes.join(" ");row.append(note);}syllables.append(row);
  });
  const problems=r.segments.filter(s=>!s.nonMyanmar&&(!s.ipa||s.status==="UNCERTAIN"||s.status==="NOT_ESTABLISHED"||s.status==="ANALYSIS_DEPENDENT"||s.uk?.status==="PROPOSED"||s.uk?.status==="ANALYSIS_DEPENDENT"));
  const preserved=r.segments.some(s=>s.nonMyanmar&&s.raw.trim()!=="");issues.hidden=problems.length===0&&!preserved;
  issueText.textContent=problems.length?"Для "+problems.length+" сегмент"+(problems.length===1?"а":"ів")+" результат містить запропоновану або неповністю встановлену відповідність; сервіс не подає її як доведену.":preserved?"Латинський текст, цифри, пробіли та пунктуацію збережено без змін; аналізуються лише сегменти Myanmar.":"";
  live.textContent="Конвертацію завершено. Статус: "+r.status;
}
source.addEventListener("input",render);
document.querySelector("#example").addEventListener("click",()=>{source.value="ကာ မြန်မာ";render();source.focus();});
document.querySelector("#clear").addEventListener("click",()=>{source.value="";render();source.focus();});
document.querySelectorAll("[data-copy]").forEach(btn=>btn.addEventListener("click",async()=>{const value=document.querySelector("#"+btn.dataset.copy).textContent;try{await navigator.clipboard.writeText(value);btn.textContent="Скопійовано";setTimeout(()=>btn.textContent="Копіювати",1200);}catch{btn.textContent="Не вдалося";}}));
render();
