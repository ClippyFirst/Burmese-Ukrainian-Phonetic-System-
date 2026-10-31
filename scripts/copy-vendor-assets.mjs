import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const source = path.join(root, "vendor", "mya2rom");
const destination = path.join(root, "public", "vendor", "mya2rom");
const required = ["romanisations.js", "mya2rom.js"];

for (const name of required) {
  const from = path.join(source, name);
  if (!fs.existsSync(from)) {
    throw new Error(`Required vendored romanizer asset is missing: ${from}`);
  }
}

fs.mkdirSync(destination, { recursive: true });
for (const name of required) {
  fs.copyFileSync(path.join(source, name), path.join(destination, name));
}

console.log("Copied Mya2Rom browser assets into Vite public output.");
