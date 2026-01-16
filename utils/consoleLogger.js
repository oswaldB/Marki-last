// utils/consoleLogger.js
module.exports = (page) => {
  page.on('console', msg => {
    const logEntry = {
      type: msg.type(),
      text: msg.text(),
      location: msg.location() ? {
        url: msg.location().url,
        line: msg.location().lineNumber,
        column: msg.location().columnNumber
      } : null,
      timestamp: new Date().toISOString()
    };

    // Affiche dans la console
    console.log(`[${logEntry.timestamp}] ${logEntry.type}: ${logEntry.text}`);
    if (logEntry.location) {
      console.log(`  @ ${logEntry.location.url}:${logEntry.location.line}:${logEntry.location.column}`);
    }

    // Optionnel : Sauvegarde dans un fichier ou une base de données
    require('fs').appendFileSync('console_logs.json', JSON.stringify(logEntry) + '\n');
  });
};