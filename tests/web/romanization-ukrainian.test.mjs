import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { renderMlctsSyllable, renderMlctsText } from "../../src/web/romanization-ukrainian.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
function parseCsv(text) {
  const lines = text.trimEnd().split(/\r?\n/u);
  const parse = (line) => {
    const cells=[]; let cell=""; let quoted=false;
    for(let i=0;i<line.length;i+=1){
      const char=line[i];
      if(char==='"'&&line[i+1]==='"'&&quoted){cell+='"';i+=1;}
      else if(char==='"')quoted=!quoted;
      else if(char===","&&!quoted){cells.push(cell);cell="";}
      else cell+=char;
    }
    cells.push(cell); assert.equal(quoted,false);
    return cells;
  };
  const headers=parse(lines.shift());
  return lines.map(line=>Object.fromEntries(headers.map((key,index)=>[key,parse(line)[index]??""])));
}

test("every inventoried MLCTS rime maps through the runtime adapter",()=>{
  const rows=parseCsv(readFileSync(path.join(root,"data/burmese/romanization_rimes_inventory.csv"),"utf8"));
  for(const row of rows){
    const result=renderMlctsSyllable(row.mlcts);
    assert.equal(result.text,row.ukrainian_candidate,row.mlcts);
    assert.equal(result.status,"PROPOSED");
    assert.equal(result.evidence,"EVIDENCE_LIMITED");
  }
});

test("all onset rows combine with an attested simple rime without losing digraphs",()=>{
  const rows=parseCsv(readFileSync(path.join(root,"data/burmese/romanization_ukrainian.csv"),"utf8"));
  for(const row of rows){
    if(!row.mlcts) continue;
    const result=renderMlctsSyllable(row.mlcts+"a");
    assert.equal(result.text,row.ukrainian_candidate+"а",row.mlcts);
  }
});

test("MLCTS medials, length and checked-syllable markers are preserved",()=>{
  assert.equal(renderMlctsSyllable("kya").text,"кйа");
  assert.equal(renderMlctsSyllable("kra").text,"крa".replace("a","а"));
  assert.equal(renderMlctsSyllable("kui:").text,"куйː");
  assert.equal(renderMlctsSyllable("aung.").text,"аунг·");
  assert.equal(renderMlctsSyllable("ip'").text,"іпʼ");
});

test("unmodelled MLCTS forms are withheld rather than guessed",()=>{
  assert.equal(renderMlctsSyllable("hlya").text,null);
  assert.equal(renderMlctsSyllable("unknown").status,"UNSUPPORTED");
});

test("text adapter preserves punctuation and non-Myanmar text",()=>{
  const result=renderMlctsText("က! ABC",()=> "ka",raw=>[{raw,nonMyanmar:false}]);
  assert.equal(result.text,"ка! ABC");
  assert.equal(result.status,"PROPOSED");
  assert.equal(result.mapped,1);
});

test("Myanmar code points outside the romanization inventory remain visible and unsupported",()=>{
  const result=renderMlctsText("ကꩠ",()=>"ka",()=>[
    {raw:"က",nonMyanmar:false},{raw:"ꩠ",nonMyanmar:false},
  ],char=>char==="က");
  assert.equal(result.text,"ка⟦ꩠ⟧");
  assert.equal(result.status,"PARTIAL");
  assert.equal(result.unsupported,1);
});


test("romanization text adapter explicitly requests orthographic MLCTS mode",()=>{
  let receivedArgs=null;
  const result=renderMlctsText("က",(...args)=>{receivedArgs=args;return "ka";},raw=>[{raw,nonMyanmar:false}]);
  assert.equal(receivedArgs[1],"mlcts");
  assert.equal(result.text,"က" ? "ка" : "");
});
