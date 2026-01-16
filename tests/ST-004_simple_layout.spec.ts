import { test, expect } from '@playwright/test';

// Test pour vérifier que la page simple charge correctement
test.describe('Simple Layout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('Doit charger la page simple avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/Simple Layout - Marki App/);
  });

  test('Doit afficher le logo Marki dans l\'en-tête', async ({ page }) => {
    const logo = page.locator('img[alt="Marki Logo"]');
    await expect(logo).toBeDefined();
  });

  test('Doit afficher les liens de navigation', async ({ page }) => {
    const homeLink = page.locator('a[href="/"]');
    await expect(homeLink).toBeDefined();

    const aboutLink = page.locator('a[href="/about"]');
    await expect(aboutLink).toBeDefined();

    const contactLink = page.locator('a[href="/contact"]');
    await expect(contactLink).toBeDefined();
  });

  test('Doit afficher le pied de page avec les informations de copyright', async ({ page }) => {
    const footer = page.locator('footer');
    await expect(footer).toBeDefined();

    const copyright = page.locator('text=🎨 Powered by MARKI');
    await expect(copyright).toBeDefined();
  });
});