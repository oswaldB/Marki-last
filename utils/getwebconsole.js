#!/usr/bin/env node

const puppeteer = require('puppeteer');

async function getWebConsole(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Écouter les messages de la console
  page.on('console', (msg) => {
    console.log(`${msg.type().toUpperCase()} ${msg.text()}`);
  });
  
  // Écouter les erreurs
  page.on('pageerror', (error) => {
    console.log(`ERREUR: ${error.message}`);
  });
  
  // Naviguer vers l'URL
  await page.goto(url, { waitUntil: 'networkidle2' });
  
  await browser.close();
}

// Récupérer l'URL depuis les arguments de la ligne de commande
const url = process.argv.find(arg => arg.startsWith('--url='))?.split('=')[1];

if (!url) {
  console.error('Veuillez fournir une URL avec --url=<URL>');
  process.exit(1);
}

getWebConsole(url).catch(err => {
  console.error('Erreur:', err);
  process.exit(1);
});
