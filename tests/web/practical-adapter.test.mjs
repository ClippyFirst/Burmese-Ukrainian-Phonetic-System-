import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { PRACTICAL } from "../../src/web/generated/data.js";
import { renderUkrainian } from "../../src/web/ukrainian-adapter.js";
const browserEngineSource = readFileSync(new URL("../../src/web/app.js", import.meta.url), "utf8");

test("browser adapter covers Ukrainian h/g/x distinctions", () => {
  for (const segment of ["h", "ɦ", "ɡ", "g", "x"]) {
    assert.ok(PRACTICAL[segment], "missing practical table row for " + segment);
  }
  assert.equal(renderUkrainian("hɦɡgx").text, "ггґґх");
});

test("browser adapter renders tied affricates as Ukrainian ц, дз, ч, дж", () => {
  const result = renderUkrainian("t͡sd͡zt͡ʃd͡ʒtɕdʑt͡ɕd͡ʑ");
  assert.equal(result.text, "цдзчджчджчдж");
  assert.equal(result.status, "PROPOSED");
});

test("browser adapter does not collapse an untied consonant sequence into an affricate", () => {
  assert.equal(renderUkrainian("ts").text, "тс");
  assert.equal(renderUkrainian("t͡s").text, "ц");
});

test("browser adapter uses Ukrainian yotated vowels after syllable-initial j", () => {
  assert.equal(renderUkrainian("ja").text, "я");
  assert.equal(renderUkrainian("je").text, "є");
  assert.equal(renderUkrainian("ji").text, "ї");
  assert.equal(renderUkrainian("jo").text, "йо");
  assert.equal(renderUkrainian("ju").text, "ю");
  assert.equal(renderUkrainian("a.ja").text, "ая");
  assert.equal(renderUkrainian("ja je ji jo ju").text, "я є ї йо ю");
});

test("browser adapter keeps tone and length in prosody trace, not practical spelling", () => {
  const result = renderUkrainian("kʰàː");
  assert.equal(result.text, "к'а");
  assert.ok(result.prosody.some((item) => item.kind === "tone"));
  assert.ok(result.prosody.some((item) => item.kind === "length"));
});

test("browser adapter omits glottal stop and withholds unknown IPA", () => {
  assert.equal(renderUkrainian("ʔa").text, "а");
  const unknown = renderUkrainian("kʰɤ");
  assert.equal(unknown.status, "NOT_ESTABLISHED");
  assert.equal(unknown.text, "");
});


test("browser engine withholds IPA and Ukrainian output for unvalidated structures", () => {
  assert.ok(browserEngineSource.includes("const unsupportedStructure=sy.kinzi||sy.kinziCoda||sy.medials.length>0||sy.conjunct.length>0"));
  assert.ok(browserEngineSource.includes('sy.uk=sy.status==="ESTABLISHED"&&sy.ipa?renderUkrainian(sy.ipa)'));
});
