import fs from "node:fs";
import path from "node:path";
const root=process.cwd();
const required=[
  "data/burmese/ukrainian_practical.csv",
  "data/burmese/practical_rules.csv",
  "data/burmese/ipa_onsets.csv",
  "data/burmese/ipa_vowels.csv",
  "data/burmese/vowel_signs.csv",
  "data/burmese/medials.csv"
];
function parseLine(line){
  const cells=[]; let cell=""; let quoted=false;
  for(let i=0;i<line.length;i++){
    const ch=line[i];
    if(ch===""" && line[i+1]===""" && quoted){cell+=""";i++;continue;}
    if(ch==="""){quoted=!quoted;continue;}
    if(ch==="," && !quoted){cells.push(cell);cell="";continue;}
    cell+=ch;
  }
  cells.push(cell);
  if(quoted) throw new Error("Unclosed CSV quote");
  return cells;
}
for(const rel of required){
  const p=path.join(root,rel);
  if(!fs.existsSync(p)) throw new Error("Missing "+rel);
  const rows=fs.readFileSync(p,"utf8").replace(/^\uFEFF/,"").trimEnd().split(/\r?\n/);
  if(rows.length<2) throw new Error("Empty dataset "+rel);
  const width=parseLine(rows[0]).length;
  for(let i=1;i<rows.length;i++) if(parseLine(rows[i]).length!==width) throw new Error("Non-rectangular CSV "+rel+" line "+(i+1));
}
console.log("web data validation: OK");
