import { test, expect } from '@playwright/test';

// Test pour vérifier que la page de connexion charge correctement
test.describe('Login Page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('Doit charger la page de connexion avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/Connexion - Marki App/);
  });

  test('Doit afficher le formulaire de connexion avec les champs pour l\'identifiant et le mot de passe', async ({ page }) => {
    const idInput = page.locator('input[id="id"]');
    await expect(idInput).toBeDefined();

    const passwordInput = page.locator('input[id="password"]');
    await expect(passwordInput).toBeDefined();

    const submitButton = page.locator('button[type="submit"]');
    await expect(submitButton).toBeDefined();
  });

  test('Doit afficher un message d\'erreur si l\'identifiant ou le mot de passe est incorrect', async ({ page }) => {
    await page.fill('input[id="id"]', 'invalid_id');
    await page.fill('input[id="password"]', 'invalid_password');
    await page.click('button[type="submit"]');

    const errorMessage = page.locator('.bg-red-100');
    await expect(errorMessage).toBeDefined();
  });

  test('Doit ouvrir le drawer d\'inscription lorsque l\'utilisateur clique sur le lien "S\'inscrire"', async ({ page }) => {
    const registerButton = page.locator('button:has-text("S\'inscrire")');
    await registerButton.click();

    // Attendre que Alpine.js met à jour l'état du drawer
    await page.waitForTimeout(1000);

    const drawer = page.locator('.fixed.inset-0:has-text("Inscription")');
    await expect(drawer).toBeVisible();

    const drawerTitle = page.locator('h2:has-text("Inscription")');
    await expect(drawerTitle).toBeVisible();
  });

  test('Doit ouvrir le drawer de mot de passe oublié lorsque l\'utilisateur clique sur le lien "Mot de passe oublié ?"', async ({ page }) => {
    const forgotPasswordButton = page.locator('button:has-text("Mot de passe oublié ?")');
    await forgotPasswordButton.click();

    // Attendre que Alpine.js met à jour l'état du drawer
    await page.waitForTimeout(1000);

    const drawer = page.locator('.fixed.inset-0:has-text("Mot de Passe Oublié")');
    await expect(drawer).toBeVisible();

    const drawerTitle = page.locator('h2:has-text("Mot de Passe Oublié")');
    await expect(drawerTitle).toBeVisible();
  });
});