import { test, expect } from "@playwright/test";

test("service loads with empty state",async({page})=>{await page.goto("/");await expect(page.locator("h1")).toContainText("Бірманський текст");await expect(page.locator("#empty")).toBeVisible();});
test("example produces result",async({page})=>{await page.goto("/");await page.click("#example");await expect(page.locator("#results")).toBeVisible();await expect(page.locator("#uk")).toBeVisible();await expect(page.locator("#ipa")).toBeVisible();});
test("source is preserved and clear works",async({page})=>{await page.goto("/");await page.locator("#source").fill("မြန်မာ ABC 123");await expect(page.locator("#source")).toHaveValue("မြန်မာ ABC 123");await page.click("#clear");await expect(page.locator("#source")).toHaveValue("");await expect(page.locator("#empty")).toBeVisible();});
test("non-Myanmar material is preserved in output",async({page})=>{await page.goto("/");await page.locator("#source").fill("မြန်မာ ABC 123!");await expect(page.locator("#uk")).toContainText(" ABC 123!");await expect(page.locator("#issues")).toContainText("збережено без змін");});
test("scientific page is reachable",async({page})=>{await page.goto("/system.html");await expect(page.locator("h1")).toContainText("українське читання");});
test("evidence status is not overstated",async({page})=>{await page.goto("/");await page.locator("#source").fill("ကာ");await expect(page.locator("#ipa")).toContainText("ka");await expect(page.locator("#uk-status")).toContainText("PROPOSED");await expect(page.locator("#issues")).toBeVisible();});
test("pure non-Myanmar input is not presented as a successful Burmese analysis",async({page})=>{await page.goto("/");await page.locator("#source").fill("ABC 123");await expect(page.locator("#uk")).toHaveText("ABC 123");await expect(page.locator("#uk-status")).toContainText("UNSUPPORTED");});
test("kinzi precedes the onset in IPA",async({page})=>{await page.goto("/");await page.locator("#source").fill("င်္ကာ");await expect(page.locator("#ipa")).toContainText("ŋka");});
test("contextual palatalization is not reduced to k+j",async({page})=>{await page.goto("/");await page.locator("#source").fill("ကျား");await expect(page.locator("#ipa")).toContainText("tɕa");});
test("closed ော vowel is derived contextually before a nasal coda",async({page})=>{await page.goto("/");await page.locator("#source").fill("ကျောင်း");await expect(page.locator("#ipa")).toContainText("tɕaʊɴ");});
test("kinzi belongs to the preceding linguistic syllable",async({page})=>{await page.goto("/");await page.locator("#source").fill("မင်္ဂလာ");await expect(page.locator("#syllables")).toContainText("မင်္");await expect(page.locator("#syllables")).toContainText("ဂ");});
test("ha-to is not blindly rendered as h on y/r initials",async({page})=>{await page.goto("/");await page.locator("#source").fill("ရှ");await expect(page.locator("#ipa")).toContainText("ʃ");});

test("nasal closed i remains short ɪ, not an overgeneralized eɪ",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ပင်");
  await expect(page.locator("#ipa")).toContainText("pɪɴ");
});

test("checked closed i becomes eɪ with a glottal coda",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("စိတ်");
  await expect(page.locator("#ipa")).toContainText("seɪʔ");
});

test("closed u with a nasal coda becomes oʊɴ",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကုန်");
  await expect(page.locator("#ipa")).toContainText("koʊɴ");
});

test("medial wa changes the rime instead of being appended as w",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကွက် ကွန်");
  await expect(page.locator("#ipa")).toContainText("kwɛʔ kwʊɴ");
});

test("i+u closed rime becomes aɪ with a glottal coda",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကိုက်");
  await expect(page.locator("#ipa")).toContainText("kaɪʔ");
});
