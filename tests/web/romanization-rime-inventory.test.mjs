import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import test from "node:test";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const vendorPath = path.join(root, "vendor/mya2rom/romanisations.js");
const csvPath = path.join(root, "data/burmese/romanization_rimes_inventory.csv");

function parseCsv(text) {
  const lines = text.trimEnd().split(/\r?\n/u);
  const headers = lines.shift().split(",");
  return lines.map((line) => {
    const cells = [];
    let cell = "";
    let quoted = false;
    for (let i = 0; i < line.length; i += 1) {
      const char = line[i];
      if (char === '"' && line[i + 1] === '"' && quoted) { cell += '"'; i += 1; }
      else if (char === '"') quoted = !quoted;
      else if (char === "," && !quoted) { cells.push(cell); cell = ""; }
      else cell += char;
    }
    cells.push(cell);
    assert.equal(quoted, false, "CSV rows must have balanced quotes");
    return Object.fromEntries(headers.map((header, i) => [header, cells[i] ?? ""]));
  });
}

function vendorMlctsRimes(source) {
  const start = source.indexOf("var vowels = {");
  const end = source.indexOf("\n}", start);
  assert.ok(start >= 0 && end > start, "vendored vowels object must exist");
  const rows = [];
  for (const line of source.slice(start, end).split(/\r?\n/u)) {
    const match = line.match(/^\s*"([^"]+)"\s*:\s*\[([^\]]+)\]/u);
    if (!match) continue;
    const values = [...match[2].matchAll(/"((?:\\.|[^"])*)"/gu)].map((item) => item[1]);
    assert.ok(values.length >= 2, "every vendor vowel row must expose an MLCTS column");
    rows.push([match[1], values[1]]);
  }
  return rows;
}

test("the 94-row MLCTS rime inventory exactly mirrors the vendored Mya2Rom MLCTS column", () => {
  const vendor = vendorMlctsRimes(readFileSync(vendorPath, "utf8"));
  const inventory = parseCsv(readFileSync(csvPath, "utf8"));
  assert.equal(vendor.length, 94);
  assert.equal(inventory.length, vendor.length);
  const actual = new Map(inventory.map((row) => [row.source_unit, row]));
  assert.equal(actual.size, inventory.length, "source-unit keys must be unique");
  for (const [sourceUnit, mlcts] of vendor) {
    const row = actual.get(sourceUnit);
    assert.ok(row, `missing vendor rime key: ${sourceUnit}`);
    assert.equal(row.mlcts, mlcts, `MLCTS value drift for ${sourceUnit}`);
    assert.equal(row.ukrainian_candidate, "", "unadjudicated targets must remain blank");
    assert.equal(row.ukrainian_status, "EVIDENCE_LIMITED");
  }
});
