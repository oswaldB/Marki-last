describe('ST-003 : Page de Login', () => {
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

  it('Doit afficher la page de login (ST-003)', () => {
    cy.visit('/login');
    cy.get('h1').should('contain', 'Login');
    cy.get('form').should('exist');
    cy.get('input[name="email"]').should('exist');
    cy.get('input[name="password"]').should('exist');
    cy.get('button[type="submit"]').should('contain', 'Se connecter');
  });

  it('Doit afficher un message d\'erreur pour des identifiants invalides (ST-003)', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('invalid@example.com');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('form').first().submit();
    
    // Attendre que le message d'erreur soit visible
    cy.get('div[class*="bg-red-100"]').should('be.visible');
    cy.get('div[class*="bg-red-100"]').should('contain', 'Email ou mot de passe incorrect');
    
    // Vérifier que nous sommes toujours sur la page de login
    cy.url().should('include', '/login');
  });

  it('Doit rediriger vers le tableau de bord après une connexion réussie (ST-003)', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('admin@example.com');
    cy.get('input[name="password"]').type('adminpassword');
    cy.get('form').first().submit();
    
    // Attendre la redirection avec un timeout plus long
    cy.url({ timeout: 5000 }).should('include', '/dashboard');
    
    // Vérifier que nous ne sommes pas redirigés vers logout
    cy.url().should('not.include', '/logout');
  });

  afterEach(() => {
    if (consoleErrors.length > 0) {
      cy.writeFile('reports/ST-003-console-errors.json', consoleErrors);
    }
  });
});