// Configuration globale pour Playwright pour capturer les logs de la console
const { exec } = require('child_process');
const { promisify } = require('util');

const execAsync = promisify(exec);

async function globalTeardown() {
  // Arrêt du serveur Flask
  await execAsync('pkill -f "python3 app.py"');
  console.log('Serveur Flask arrêté.');
}

module.exports = globalTeardown;