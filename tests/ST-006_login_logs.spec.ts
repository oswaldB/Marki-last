import { test, expect } from '@playwright/test';
import { PickleDB } from 'pickledb';

// Test pour vérifier que les logs sont bien enregistrés dans PickleDB
test.describe('Login Logs (PickleDB)', () => {
  test('Doit enregistrer un log de connexion dans PickleDB', async ({ page }) => {
    // Se connecter avec un utilisateur valide
    await page.goto('/login');
    await page.fill('input[id="id"]', 'user1');
    await page.fill('input[id="password"]', 'password123');
    await page.click('button[type="submit"]');
    
    // Vérifier que l'utilisateur est redirigé vers le dashboard
    await expect(page).toHaveURL('/app/dashboard');
    
    // Vérifier que le log a été enregistré dans PickleDB
    const logs_db = new PickleDB('/app/logs.db');
    const log_key = 'user_1';
    const logs = logs_db.get(log_key);
    
    expect(logs).toBeDefined();
    expect(logs.length).toBeGreaterThan(0);
    expect(logs[logs.length - 1].action).toBe('login');
    expect(logs[logs.length - 1].details).toBe('User logged in successfully');
  });

  test('Doit enregistrer un log de déconnexion dans PickleDB', async ({ page }) => {
    // Se connecter avec un utilisateur valide
    await page.goto('/login');
    await page.fill('input[id="id"]', 'user1');
    await page.fill('input[id="password"]', 'password123');
    await page.click('button[type="submit"]');
    
    // Se déconnecter
    await page.goto('/logout');
    
    // Vérifier que l'utilisateur est redirigé vers la page de connexion
    await expect(page).toHaveURL('/login');
    
    // Vérifier que le log a été enregistré dans PickleDB
    const logs_db = new PickleDB('/app/logs.db');
    const log_key = 'user_1';
    const logs = logs_db.get(log_key);
    
    expect(logs).toBeDefined();
    expect(logs.length).toBeGreaterThan(0);
    expect(logs[logs.length - 1].action).toBe('logout');
    expect(logs[logs.length - 1].details).toBe('User logged out successfully');
  });
});
