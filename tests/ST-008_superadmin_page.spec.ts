import { test, expect } from '@playwright/test';
import setupConsoleLogger from '../utils/consoleLogger';

// Test pour vérifier que la page SuperAdmin charge correctement
test.describe('SuperAdmin Page', () => {
  test.beforeEach(async ({ page }) => {
    // Configuration de la capture des logs console
    setupConsoleLogger(page);
    
    await page.goto('http://127.0.0.1:5000/superadmin');
    await page.waitForLoadState('networkidle');
  });

  test('Doit charger la page SuperAdmin avec succès', async ({ page }) => {
    await expect(page).toHaveTitle(/SuperAdmin - Marki App/);
  });

  test('Doit afficher le champ de mot de passe de protection', async ({ page }) => {
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await expect(protectionCodeInput).toBeDefined();

    const validateButton = page.locator('button:has-text("Valider")');
    await expect(validateButton).toBeDefined();
  });

  test('Doit afficher les composants de gestion des utilisateurs après validation du mot de passe', async ({ page }) => {
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await protectionCodeInput.fill('Citron6-Mustang9');

    const validateButton = page.locator('button:has-text("Valider")');
    await validateButton.click();

    const userManagementSection = page.locator('h2:has-text("Gestion des Utilisateurs")');
    await expect(userManagementSection).toBeDefined();

    const userListSection = page.locator('h2:has-text("Liste des Utilisateurs")');
    await expect(userListSection).toBeDefined();
  });

  test('Doit afficher un message d\'erreur si le mot de passe de protection est incorrect', async ({ page }) => {
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await protectionCodeInput.fill('incorrect_password');

    const validateButton = page.locator('button:has-text("Valider")');
    await validateButton.click();

    // Vérifier que les composants de gestion des utilisateurs ne sont pas visibles
    const userManagementSection = page.locator('h2:has-text("Gestion des Utilisateurs")');
    await expect(userManagementSection).not.toBeVisible();

    const userListSection = page.locator('h2:has-text("Liste des Utilisateurs")');
    await expect(userListSection).not.toBeVisible();
  });

  test('Doit permettre la création d\'un nouvel utilisateur', async ({ page }) => {
    // Valider le mot de passe de protection
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await protectionCodeInput.fill('Citron6-Mustang9');

    const validateButton = page.locator('button:has-text("Valider")');
    await validateButton.click();

    // Remplir le formulaire de création d'utilisateur
    const userIdInput = page.locator('input[id="user-id"]');
    await userIdInput.fill('new_user');

    const userPasswordInput = page.locator('input[id="user-password"]');
    await userPasswordInput.fill('new_password');

    const isAdminCheckbox = page.locator('input[type="checkbox"]');
    await isAdminCheckbox.check();

    const createButton = page.locator('button:has-text("Créer")');
    await createButton.click();

    // Vérifier que l'utilisateur a été créé avec succès
    const successMessage = page.locator('text=Utilisateur créé avec succès.');
    await expect(successMessage).toBeDefined();
  });

  test('Doit permettre l\'activation d\'un utilisateur', async ({ page }) => {
    // Valider le mot de passe de protection
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await protectionCodeInput.fill('Citron6-Mustang9');

    const validateButton = page.locator('button:has-text("Valider")');
    await validateButton.click();

    // Cliquer sur le bouton d'activation du premier utilisateur
    const activateButton = page.locator('button:has-text("Activer")').first();
    await activateButton.click();

    // Vérifier que l'utilisateur a été activé avec succès
    const successMessage = page.locator('text=Utilisateur activé avec succès.');
    await expect(successMessage).toBeDefined();
  });

  test('Doit permettre la modification du mot de passe d\'un utilisateur', async ({ page }) => {
    // Valider le mot de passe de protection
    const protectionCodeInput = page.locator('input[id="protection-code"]');
    await protectionCodeInput.fill('Citron6-Mustang9');

    const validateButton = page.locator('button:has-text("Valider")');
    await validateButton.click();

    // Cliquer sur le bouton de modification du premier utilisateur
    const modifyButton = page.locator('button:has-text("Modifier")').first();
    await modifyButton.click();

    // Saisir le nouveau mot de passe
    await page.on('dialog', dialog => {
      dialog.accept('new_password');
    });

    // Vérifier que le mot de passe a été modifié avec succès
    const successMessage = page.locator('text=Mot de passe modifié avec succès.');
    await expect(successMessage).toBeDefined();
  });
});