import test from "node:test";
import assert from "node:assert/strict";
import { ONSETS, VOWELS, SIGNS, MEDIALS, PRACTICAL, RULES } from "../../src/web/generated/data.js";
test("generated inventories",()=>{assert.equal(ONSETS["က"].ipa,"k");assert.equal(ONSETS["င"].ipa,"ŋ");assert.equal(VOWELS.i?.ipa,"i");assert.ok(SIGNS["ေ"]);assert.equal(MEDIALS["ျ"].id,"medial_ya");});
test("practical data is source-backed",()=>{assert.equal(PRACTICAL["k"][0].ukrainian_candidate,"к");assert.equal(PRACTICAL["kʰ"][0].ukrainian_candidate,"к");assert.ok(RULES["kʰ"]);});
