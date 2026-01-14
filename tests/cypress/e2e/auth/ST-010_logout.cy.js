describe('ST-010 : Bouton de Déconnexion', () => {
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

  it('Doit afficher le bouton de déconnexion dans le menu utilisateur (ST-010)', () => {
    // Se connecter d'abord
    cy.visit('/login');
    cy.get('input[name="username"]').type('oswald');
    cy.get('input[name="password"]').type('coucou');
    cy.get('form').first().submit();
    
    // Attendre la redirection vers le tableau de bord
    cy.url({ timeout: 10000 }).should('include', '/dashboard');
    
    // Attendre que la page soit complètement chargée
    cy.wait(2000);
    
    // Ouvrir le menu utilisateur - utiliser un sélecteur plus spécifique
    cy.get('button[class*="flex items-center"]').contains('o').click();
    
    // Vérifier que le bouton de déconnexion est visible
    cy.get('button[type="submit"]').contains('Déconnexion').should('be.visible');
    cy.get('button[type="submit"]').contains('Déconnexion').should('have.class', 'text-error');
  });

  it('Doit déconnecter l\'utilisateur et rediriger vers la page de login (ST-010)', () => {
    // Se connecter d'abord
    cy.visit('/login');
    cy.get('input[name="username"]').type('oswald');
    cy.get('input[name="password"]').type('coucou');
    cy.get('form').first().submit();
    
    // Attendre la redirection vers le tableau de bord
    cy.url({ timeout: 10000 }).should('include', '/dashboard');
    
    // Attendre que la page soit complètement chargée
    cy.wait(2000);
    
    // Ouvrir le menu utilisateur
    cy.get('button[class*="flex items-center"]').contains('o').click();
    
    // Cliquer sur le bouton de déconnexion
    cy.get('button[type="submit"]').contains('Déconnexion').click();
    
    // Attendre la redirection vers la page de login
    cy.url({ timeout: 10000 }).should('include', '/login');
    
    // Vérifier que l'utilisateur est bien déconnecté en essayant d'accéder au tableau de bord
    cy.visit('/dashboard');
    cy.url({ timeout: 10000 }).should('include', '/login');
  });

  it('Doit afficher un message de confirmation après la déconnexion (ST-010)', () => {
    // Se connecter d'abord
    cy.visit('/login');
    cy.get('input[name="username"]').type('oswald');
    cy.get('input[name="password"]').type('coucou');
    cy.get('form').first().submit();
    
    // Attendre la redirection vers le tableau de bord
    cy.url({ timeout: 10000 }).should('include', '/dashboard');
    
    // Attendre que la page soit complètement chargée
    cy.wait(2000);
    
    // Ouvrir le menu utilisateur
    cy.get('button[class*="flex items-center"]').contains('o').click();
    
    // Cliquer sur le bouton de déconnexion
    cy.get('button[type="submit"]').contains('Déconnexion').click();
    
    // Attendre la redirection vers la page de login
    cy.url({ timeout: 10000 }).should('include', '/login');
    
    // Vérifier que le message de confirmation est affiché
    cy.get('div[class*="bg-green-100"]').should('be.visible');
    cy.get('div[class*="bg-green-100"]').should('contain', 'Vous avez été déconnecté avec succès');
  });

  afterEach(() => {
    if (consoleErrors.length > 0) {
      cy.writeFile('reports/ST-010-console-errors.json', consoleErrors);
    }
  });
});