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

test("medial wa with a sonorant coda uses the closed u-like rime",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ဆွမ်း");
  await expect(page.locator("#ipa")).toContainText("sʰwʊɴ");
});

test("Myanmar Extended-B characters are recognized as Myanmar script, then explicitly marked unsupported",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ꩠ");
  await expect(page.locator("#uk-status")).toContainText("UNSUPPORTED");
  await expect(page.locator("#issues")).not.toContainText("збережено без змін");
});

test("mixed Myanmar and supplementary-block Myanmar material does not silently become ordinary passthrough",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("မြန်မာ ꩠ");
  await expect(page.locator("#uk-status")).toContainText("UNSUPPORTED");
  await expect(page.locator("#issues")).not.toContainText("збережено без змін");
});

test("aspirated onset IPA is tokenized and receives a Ukrainian candidate",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ဆာ");
  await expect(page.locator("#ipa")).toContainText("sʰa");
  await expect(page.locator("#uk")).toContainText("са");
  await expect(page.locator("#uk-status")).toContainText("PROPOSED");
});

test("theta IPA is tokenized through its explicitly marked candidate rule",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("သာ");
  await expect(page.locator("#ipa")).toContainText("θa");
  await expect(page.locator("#uk")).toContainText("та");
  await expect(page.locator("#uk-status")).toContainText("ANALYSIS_DEPENDENT");
});

test("kinzi coda is parsed as part of the preceding syllable",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("မင်္ဂလာ");
  await expect(page.locator("#ipa")).toContainText("mɪɴɡala");
  await expect(page.locator("#syllables")).not.toContainText("Нерозібраний знак");
});

test("Burmese comma and full stop do not make a recognized word uncertain",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကျောင်း၊ ကျောင်း။");
  await expect(page.locator("#ipa")).toContainText("tɕaʊɴ");
  await expect(page.locator("#uk")).not.toContainText("∅");
  await expect(page.locator("#syllables")).not.toContainText("Нерозібраний знак ၊");
  await expect(page.locator("#syllables")).not.toContainText("Нерозібраний знак ။");
});

test("diphthongs and null checked codas render as readable Ukrainian, not debug symbols",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကျောင်း စိတ် ပိုက် ကိုက်");
  await expect(page.locator("#uk")).toContainText("чаунг");
  await expect(page.locator("#uk")).not.toContainText("∅");
});

test("non-Myanmar runs are grouped instead of displayed one character at a time",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ABC 123 — Test #42");
  await expect(page.locator("#syllables .syllable")).toHaveCount(1);
  await expect(page.locator("#syllables .syllable").first()).toContainText("ABC 123 — Test #42");
});

test("မြန်မာ separates into syllable-like clusters without false unsupported-sign warnings",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("မြန်မာ");
  await expect(page.locator("#syllables")).not.toContainText("Нерозібраний знак");
  await expect(page.locator("#syllables")).not.toContainText("UNSUPPORTED");
});

test("provisional Ukrainian mappings are visible in segment-level evidence status",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကာ");
  await expect(page.locator("#uk-status")).toContainText("PROPOSED");
  await expect(page.locator("#syllables")).toContainText("передача: PROPOSED");
});

test("a mixed string keeps the most cautious mapping status in the aggregate",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကာ သာ");
  await expect(page.locator("#uk-status")).toContainText("ANALYSIS_DEPENDENT");
});


test("open E vowel sign is analyzed and rendered as a provisional Ukrainian candidate",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကေ");
  await expect(page.locator("#ipa")).toContainText("ke");
  await expect(page.locator("#uk")).toContainText("ке");
  await expect(page.locator("#uk-status")).toContainText("PROPOSED");
});

test("the conventional ော် rime does not become an unsupported checked coda",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကော်");
  await expect(page.locator("#ipa")).toContainText("kɔ");
  await expect(page.locator("#uk")).toContainText("ко");
  await expect(page.locator("#ipa")).not.toContainText("?");
});

test("the ည် rime after a ya/ra medial is not misread as a velar nasal ending",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကြည်");
  await expect(page.locator("#ipa")).toContainText("tɕɪ");
  await expect(page.locator("#ipa")).not.toContainText("tɕaɴ");
  await expect(page.locator("#uk")).toContainText("чи");
});

test("the E-plus-yat rime in စွယ် is parsed without inventing a final glide",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("စွယ်");
  await expect(page.locator("#ipa")).toContainText("swɛ");
  await expect(page.locator("#ipa")).not.toContainText("?");
  await expect(page.locator("#uk")).toContainText("све");
});


test("phonological and Ukrainian-candidate evidence statuses are reported independently",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကာ");
  await expect(page.locator("#uk-status")).toContainText("IPA: ESTABLISHED");
  await expect(page.locator("#uk-status")).toContainText("українська передача: PROPOSED");
});

test("prosodic markers are summarized once instead of repeated in every segment row",async({page})=>{
  await page.goto("/");
  await page.locator("#source").fill("ကျောင်း၊ ကျောင်း။");
  await expect(page.locator("#issues")).toContainText("Просодичні знаки збережено в аналітичному шарі");
  await expect(page.locator("#syllables")).not.toContainText("Просодичний/ритмічний знак збережено як аналітичний маркер");
});
