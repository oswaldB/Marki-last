describe('ST-009 : Page Dashboard', () => {
  const consoleErrors = [];

  beforeEach(() => {
    cy.on('uncaught:exception', (err) => {
      consoleErrors.push({
        name: err.name,
        message: err.message,
        stack: err.stack,
      });
      return false;
    });
  });

  it('Doit afficher la page dashboard avec un message de bienvenue (ST-009)', () => {
    // Visiter la page dashboard
    cy.visit('/dashboard');
    
    // Vérifier que la page est chargée dans le layout principal
    cy.get('body').should('contain', 'Bonjour');
    
    // Vérifier la présence des éléments principaux
    cy.contains('h1', 'Tableau de Bord').should('be.visible');
    cy.contains('Bienvenue').should('be.visible');
    
    // Vérifier que la sidebar et topbar sont présentes
    cy.get('aside').should('exist');
    cy.get('header').should('exist');
  });

  it('Doit être accessible uniquement aux utilisateurs authentifiés (ST-009)', () => {
    // Déconnexion si nécessaire
    cy.visit('/logout');
    
    // Tentative d'accès au dashboard sans authentification
    cy.visit('/dashboard', { failOnStatusCode: false });
    
    // Doit être redirigé vers la page de login
    cy.url().should('include', '/login');
  });

  afterEach(() => {
    if (consoleErrors.length > 0) {
      cy.writeFile('reports/ST-009-console-errors.json', consoleErrors);
    }
  });
});