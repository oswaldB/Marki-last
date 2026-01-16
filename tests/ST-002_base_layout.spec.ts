import { test, expect } from '@playwright/test';

// Test pour vérifier que la page de base charge correctement
// et que les dépendances CDN sont présentes
test.describe('Base Layout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('Doit charger la page de base avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/Marki App/);
  });

  test('Doit inclure Tailwind CSS via CDN', async ({ page }) => {
    const tailwindScript = page.locator('script[src="https://cdn.tailwindcss.com"]');
    await expect(tailwindScript).toBeDefined();
  });

  test('Doit inclure Alpine.js via CDN', async ({ page }) => {
    const alpineScript = page.locator('script[src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"]');
    await expect(alpineScript).toBeDefined();
  });

  test('Doit inclure Lucid Icons via CDN', async ({ page }) => {
    const lucidLink = page.locator('link[href="https://unpkg.com/lucide@latest/dist/lucide.css"]');
    await expect(lucidLink).toBeDefined();
  });
});