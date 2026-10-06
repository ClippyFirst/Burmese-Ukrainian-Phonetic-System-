import { test, expect } from "@playwright/test";
test("service loads with empty state",async({page})=>{await page.goto("/");await expect(page.locator("h1")).toContainText("Бірманський текст");await expect(page.locator("#empty")).toBeVisible();});
test("example produces result",async({page})=>{await page.goto("/");await page.click("#example");await expect(page.locator("#results")).toBeVisible();await expect(page.locator("#uk")).toBeVisible();await expect(page.locator("#ipa")).toBeVisible();});
test("source is preserved and clear works",async({page})=>{await page.goto("/");await page.locator("#source").fill("မြန်မာ ABC 123");await expect(page.locator("#source")).toHaveValue("မြန်မာ ABC 123");await page.click("#clear");await expect(page.locator("#source")).toHaveValue("");await expect(page.locator("#empty")).toBeVisible();});
test("scientific page is reachable",async({page})=>{await page.goto("/system.html");await expect(page.locator("h1")).toContainText("українське читання");});
