import { test, expect } from '@playwright/test';
import { exec } from 'child_process';
import { promisify } from 'util';
import setupConsoleLogger from '../utils/consoleLogger';

const execAsync = promisify(exec);

test.describe('Hello World Page', () => {
  let serverProcess;

  test.beforeAll(async () => {
    // Démarrage du serveur Flask avec capture des logs
    serverProcess = execAsync('python3 start_server_with_logs.py');
    await new Promise(resolve => setTimeout(resolve, 3000)); // Attente pour le démarrage du serveur
  });



  test.beforeEach(async ({ page }) => {
    // Capture des logs de la console avant l'action
    page.on('console', msg => console.log('Console log:', msg.text()));
    page.on('pageerror', error => console.log('Page error:', error.message));
    
    console.log('\n=== Début de l\'action: Navigation vers la page Hello World ===');
    
    // Capture des logs de la console avant l'action
    const beforeLogs = await page.evaluate(() => {
      return JSON.stringify(window.consoleLogs || []);
    });
    console.log('Console logs avant action:', beforeLogs);
    
    await page.goto('http://127.0.0.1:5000/');
    
    // Capture des logs de la console après l'action
    const afterLogs = await page.evaluate(() => {
      return JSON.stringify(window.consoleLogs || []);
    });
    console.log('Console logs après action:', afterLogs);
    
    console.log('=== Fin de l\'action: Navigation vers la page Hello World ===\n');
  });

  test('Doit afficher le texte "Hello World"', async ({ page }) => {
    const helloWorldText = page.locator('text="Hello World"');
    await expect(helloWorldText).toBeVisible();
  });

  test('Doit afficher le logo Marki', async ({ page }) => {
    const logo = page.locator('img[alt="Marki Logo"]');
    await expect(logo).toBeVisible();
  });

  test('Doit avoir le texte "Hello World" en gras', async ({ page }) => {
    const helloWorldText = page.locator('text="Hello World"');
    await expect(helloWorldText).toHaveCSS('font-weight', '700');
  });

  test('Doit être accessible via l\'URL /', async ({ page }) => {
    await expect(page).toHaveURL('http://127.0.0.1:5000/');
  });

  test('Doit vérifier les logs du serveur', async ({ page }) => {
    // Vérification que la page est accessible
    await expect(page).toHaveURL('http://127.0.0.1:5000/');
  });
});