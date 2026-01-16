import { test, expect } from '@playwright/test';

// Test pour vérifier que la page de dashboard charge correctement
test.describe('Dashboard Layout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/dashboard');
  });

  test('Doit charger la page de dashboard avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/Dashboard - Marki App/);
  });

  test('Doit afficher la sidebar avec les liens de navigation', async ({ page }) => {
    const sidebar = page.locator('.w-64.bg-gray-800');
    await expect(sidebar).toBeDefined();

    const homeLink = page.locator('a[href="/dashboard"]');
    await expect(homeLink).toBeDefined();

    const profileLink = page.locator('a[href="/dashboard/profile"]');
    await expect(profileLink).toBeDefined();

    const logoutLink = page.locator('a[href="/logout"]');
    await expect(logoutLink).toBeDefined();
  });

  test('Doit afficher la topbar avec les informations de l\'utilisateur', async ({ page }) => {
    const topbar = page.locator('.bg-white.shadow');
    await expect(topbar).toBeDefined();

    const userInfo = page.locator('span:has-text("Utilisateur:")');
    await expect(userInfo).toBeDefined();

    const logoutButton = page.locator('a.bg-red-500');
    await expect(logoutButton).toBeDefined();
  });
});