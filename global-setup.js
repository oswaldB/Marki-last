// Configuration globale pour Playwright pour capturer les logs de la console
const { chromium } = require('playwright');

async function globalSetup() {
  // Capture des logs de la console
  const browser = await chromium.launch({
    args: ['--enable-logging'],
  });
  
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // Capture des logs de la console
  page.on('console', msg => console.log('Console log:', msg.text()));
  page.on('pageerror', error => console.log('Page error:', error.message));
  
  // Navigation vers la page de base
  await page.goto('http://127.0.0.1:5000/');
  
  // Vérification des logs de la console
  const consoleLogs = await page.evaluate(() => {
    return JSON.stringify(window.consoleLogs || []);
  });
  console.log('Console logs après navigation:', consoleLogs);
  
  await browser.close();
}

module.exports = globalSetup;