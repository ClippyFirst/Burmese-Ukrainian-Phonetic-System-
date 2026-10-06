import { ONSETS, SIGNS, MEDIALS, PRACTICAL, RULES } from "./generated/data.js";

const source=document.querySelector("#source"), results=document.querySelector("#results"), empty=document.querySelector("#empty");
const issues=document.querySelector("#issues"), issueText=document.querySelector("#issue-text"), count=document.querySelector("#count");
const uk=document.querySelector("#uk"), ipa=document.querySelector("#ipa"), syllables=document.querySelector("#syllables");
const ukStatus=document.querySelector("#uk-status"), ipaStatus=document.querySelector("#ipa-status"), live=document.querySelector("#live");

const KINZI="င်္", VIRAMA="္", ASAT="်";
const NASAL_CODAS=new Set(["င","န","မ","ည"]);
const CHECKED_CODAS=new Set(["က","ခ","ဂ","ဃ","စ","ဆ","ဇ","ဈ","တ","ထ","ဒ","ဓ","ပ","ဖ","ဗ","ဘ"]);
const IPA_UNIT_RE=/t͡?ɕʰ|t͡?ɕ|d͡?ʑ|m̥|n̥|ŋ̊|ɲ̥|l̥|ʍ|ʃ|ɴ|ŋ|ɲ|ɯ|ɛ|ɪ|ɔ|ə|ʊ|eɪ|oʊ|aɪ|aʊ|[a-zɡʔː]/g;
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
      const followsKinzi=s.slice(Math.max(start,i-3),i)===KINZI;
      const isNewBase=BASE.has(s[i])&&!isCodaBase&&prev!==ASAT&&(prev!==VIRAMA||followsKinzi);
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
  // Dependent vowels belong to the preceding linguistic syllable; a following
  // kinzi is its final /ŋ/, even though the Unicode sequence is stored before
  // the next written base consonant.
  while(i<raw.length&&VOWEL_CHARS.has(raw[i]))sy.vowels.push(raw[i++]);
  if(i+2<raw.length&&raw.slice(i,i+3)===KINZI){sy.kinziCoda=true;sy.coda="င";i+=3;sy.asat=true;}
  if(!sy.coda&&i+1<raw.length&&BASE.has(raw[i])&&raw[i+1]===ASAT){sy.coda=raw[i];i+=2;sy.asat=true;}
  while(i<raw.length){
    if(raw[i]===ASAT){sy.asat=true;i++;continue;}
    if(raw[i]==="ံ"||raw[i]==="့"||raw[i]==="း"){sy.notes.push("Просодичний/ритмічний знак збережено як аналітичний маркер.");sy.status="ANALYSIS_DEPENDENT";i++;continue;}
    sy.status="UNCERTAIN";sy.notes.push("Нерозібраний знак "+raw[i++]);
  }
  sy.ipa=deriveIpa(sy);if(!sy.ipa&&sy.status==="ESTABLISHED")sy.status="NOT_ESTABLISHED";sy.uk=renderUkrainian(sy.ipa);return sy;
}

function deriveIpa(sy){
  const onset=ONSETS[sy.onset];if(!onset)return null;
  let initial=onset.ipa;const parts=[];
  if(sy.kinzi)parts.push("ŋ");
  const ids=sy.medials.map(m=>MEDIALS[m]?.id).filter(Boolean);
  const has=key=>ids.includes(key);
  const coda=sy.coda;
  const nasalCoda=!!coda&&NASAL_CODAS.has(coda);
  const checkedCoda=!!coda&&CHECKED_CODAS.has(coda);
  if(has("medial_ya")||has("medial_ra")){
    if(initial==="k")initial="tɕ";
    else if(initial==="kʰ")initial="tɕʰ";
    else if(initial==="ɡ")initial="dʑ";
    else if(initial==="ŋ"&&has("medial_ra"))initial="ɲ";
  }
  if(has("medial_ha")){
    const devoiced={m:"m̥",n:"n̥","ŋ":"ŋ̊","ɲ":"ɲ̥",l:"l̥",w:"ʍ"};
    if(initial==="j"||initial==="r")initial="ʃ";
    else if(devoiced[initial])initial=devoiced[initial];
    else return null;
  }
  parts.push(initial);
  const wa=has("medial_wa");
  const vowelIds=sy.vowels.map(sign=>SIGNS[sign]?.unicode_name).filter(Boolean);
  const hasV=id=>vowelIds.includes(id);
  const closed=!!coda||sy.asat;
  let vowel=null;
  if(hasV("MYANMAR VOWEL SIGN E")&&(hasV("MYANMAR VOWEL SIGN AA")||hasV("MYANMAR VOWEL SIGN TALL AA"))){
    vowel=closed?(nasalCoda||checkedCoda?"aʊ":null):"ɔ";
  }else if(hasV("MYANMAR VOWEL SIGN I")&&hasV("MYANMAR VOWEL SIGN U")){
    vowel=closed?"aɪ":"o";
  }else if(hasV("MYANMAR VOWEL SIGN I")){
    if(wa&&closed)vowel=nasalCoda?"ʊ":checkedCoda?"ɛ":null;
    else if(checkedCoda)vowel="eɪ";
    else if(nasalCoda)vowel="ɪ";
    else vowel="i";
  }else if(hasV("MYANMAR VOWEL SIGN II")){
    vowel=closed?"i":"iː";
  }else if(hasV("MYANMAR VOWEL SIGN U")){
    if(wa&&closed)vowel="ʊ";
    else if(closed)vowel="oʊ";
    else vowel="u";
  }else if(hasV("MYANMAR VOWEL SIGN UU")){
    vowel=closed?"oʊ":"uː";
  }else if(hasV("MYANMAR VOWEL SIGN AI")){
    vowel="ɛ";
  }else if(hasV("MYANMAR VOWEL SIGN TALL AA")||hasV("MYANMAR VOWEL SIGN AA")){
    if(wa&&closed)vowel=nasalCoda?"ʊ":checkedCoda?"ɛ":null;
    else vowel="a";
  }else if(hasV("MYANMAR SIGN ANUSVARA")){
    vowel=nasalCoda?"ɪ":"a";
  }
  if(!vowel){
    if(!sy.vowels.length&&wa&&nasalCoda)vowel="ʊ";
    else if(!sy.vowels.length&&wa&&checkedCoda)vowel="ɛ";
    else if(!sy.vowels.length&&!sy.coda&&!sy.asat)vowel="a";
    else if(sy.kinziCoda&&!sy.vowels.length)vowel="ɪ";
    else return null;
  }
  parts.push(vowel);
  if(coda){
    if(nasalCoda)parts.push("ɴ");
    else if(checkedCoda)parts.push("ʔ");
    else if(coda==="ယ"||coda==="ရ")parts.push("j");
    else if(coda==="လ")parts.push("l");
    else if(coda==="ဝ")parts.push("w");
    else return null;
  }
  return parts.join("");
}

function candidateFor(segment){
  const direct=PRACTICAL[segment]||PRACTICAL[segment==="θ"?"θ~ð":segment]||PRACTICAL[segment==="ɴ"?"ŋ":segment];
  if(!direct)return{text:"",status:"NOT_ESTABLISHED",reason:"Немає точного правила для цього IPA-сегмента."};
  const row=direct[0];
  return{text:row.ukrainian_candidate,status:(row.status||"UNKNOWN").toUpperCase(),reason:row.policy,ruleIds:(RULES[segment]||RULES["/"+segment+"/"]||[]).map(x=>x.rule_id)};
}

function renderUkrainian(ipaText){
  if(!ipaText)return{text:"",status:"NOT_ESTABLISHED",parts:[]};
  const units=ipaText.match(IPA_UNIT_RE)||[];
  if(units.join("")!==ipaText)return{text:"",status:"NOT_ESTABLISHED",parts:[]};
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
