import { test, expect } from '@playwright/test';

test.describe('Hello World Page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://127.0.0.1:5000/');
  });

  test('Doit afficher le texte "Hello World"', async ({ page }) => {
    const helloWorldText = page.locator('text="Hello World"');
    await expect(helloWorldText).toBeVisible();
  });

  test('Doit afficher le logo Marki', async ({ page }) => {
    const logo = page.locator('img[alt="Marki"]');
    await expect(logo).toBeVisible();
  });

  test('Doit avoir le texte "Hello World" en gras', async ({ page }) => {
    const helloWorldText = page.locator('text="Hello World"');
    await expect(helloWorldText).toHaveCSS('font-weight', '700');
  });

  test('Doit être accessible via l\'URL /', async ({ page }) => {
    await expect(page).toHaveURL('http://127.0.0.1:5000/');
  });
});