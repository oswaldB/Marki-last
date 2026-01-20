// Configuration de Playwright pour capturer les logs de la console
const config = {
  // Options de base
  testDir: './tests',
  timeout: 30000,
  retries: 0,
  
  // Options pour capturer les logs de la console
  use: {
    baseURL: 'http://127.0.0.1:5000',
    // Capture des logs de la console
    trace: 'on',
    video: 'on',
    screenshot: 'on',
    
    // Options pour capturer les logs de la console
    launchOptions: {
      args: ['--enable-logging'],
    },
    
    // Options pour capturer les logs de la console
    contextOptions: {
      ignoreHTTPSErrors: true,
    },
  },
  
  // Options pour capturer les logs de la console
  reporter: [
    ['line'],
    ['json', { outputFile: 'test-results/results.json' }],
  ],
  
  // Options pour capturer les logs de la console
  globalSetup: './global-setup.js',
  globalTeardown: './global-teardown.js',
  
  // Options pour capturer les logs de la console avant et après chaque test
  expect: {
    toHaveConsoleLogs: async (page, expectedLogs) => {
      const consoleLogs = await page.evaluate(() => {
        return JSON.stringify(window.consoleLogs || []);
      });
      expect(consoleLogs).toContain(expectedLogs);
    },
  },
};

module.exports = config;