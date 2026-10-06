import fs from "node:fs";
import path from "node:path";
const root=process.cwd();
const required=["data/burmese/ukrainian_practical.csv","data/burmese/practical_rules.csv","data/burmese/ipa_onsets.csv","data/burmese/ipa_vowels.csv","data/burmese/vowel_signs.csv","data/burmese/medials.csv"];
for(const rel of required){
  const p=path.join(root,rel);
  if(!fs.existsSync(p)) throw new Error("Missing "+rel);
  const text=fs.readFileSync(p,"utf8").replace(/^\uFEFF/,"");
  const rows=text.trimEnd().split(/\r?\n/);
  if(rows.length<2) throw new Error("Empty dataset "+rel);
  const width=rows[0].split(",").length;
  for(let i=1;i<rows.length;i++) if(rows[i].split(",").length!==width) throw new Error("Non-rectangular CSV "+rel+" line "+(i+1));
}
console.log("web data validation: OK");
