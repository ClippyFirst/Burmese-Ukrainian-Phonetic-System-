import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const dist = path.join(root, "dist");

test("production Pages artifact contains both site pages and the Mya2Rom browser assets", () => {
  assert.ok(existsSync(path.join(dist, "index.html")), "service page must be in dist");
  assert.ok(existsSync(path.join(dist, "system.html")), "methodology page must be in dist");
  assert.ok(existsSync(path.join(dist, "vendor", "mya2rom", "romanisations.js")), "Mya2Rom romanisation table must be copied into dist");
  assert.ok(existsSync(path.join(dist, "vendor", "mya2rom", "mya2rom.js")), "Mya2Rom browser engine must be copied into dist");
  const serviceHtml = readFileSync(path.join(dist, "index.html"), "utf8");
  assert.match(serviceHtml, /vendor\/mya2rom\/romanisations\.js/);
  assert.match(serviceHtml, /vendor\/mya2rom\/mya2rom\.js/);
});
