import { test, expect } from '@playwright/test';

// Test pour vérifier que la page simple avec authentification charge correctement
test.describe('Simple Auth Layout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/profile');
  });

  test('Doit charger la page simple avec authentification avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/Simple Auth Layout - Marki App/);
  });

  test('Doit afficher le logo Marki dans l\'en-tête', async ({ page }) => {
    const logo = page.locator('img[alt="Marki Logo"]');
    await expect(logo).toBeDefined();
  });

  test('Doit afficher les liens de navigation pour les utilisateurs authentifiés', async ({ page }) => {
    const dashboardLink = page.locator('a[href="/dashboard"]');
    await expect(dashboardLink).toBeDefined();

    const profileLink = page.locator('a[href="/profile"]');
    await expect(profileLink).toBeDefined();

    const logoutLink = page.locator('a[href="/logout"]');
    await expect(logoutLink).toBeDefined();
  });

  test('Doit afficher le pied de page avec les informations de copyright', async ({ page }) => {
    const footer = page.locator('footer');
    await expect(footer).toBeDefined();

    const copyright = page.locator('text=🎨 Powered by MARKI');
    await expect(copyright).toBeDefined();
  });
});