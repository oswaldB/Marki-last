// Utilitaires pour Playwright pour capturer les logs de la console
const { captureConsoleLogs } = require('./global-setup');

// Fonction pour capturer les logs de la console avant et après chaque action
async function withConsoleLogs(page, actionName, action) {
  await captureConsoleLogs(page, actionName);
  await action();
  await captureConsoleLogs(page, actionName);
}

// Fonction pour capturer les logs de la console avant et après chaque test
async function withTestConsoleLogs(page, testName, test) {
  console.log(`\n=== Début du test: ${testName} ===`);
  await test();
  console.log(`=== Fin du test: ${testName} ===\n`);
}

module.exports = { withConsoleLogs, withTestConsoleLogs };