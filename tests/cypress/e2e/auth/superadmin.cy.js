describe('ST-008 : Page Superadmin', () => {
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

  it('Doit afficher le formulaire de création du superadmin (ST-008)', () => {
    cy.visit('/superadmin');
    cy.get('input[id="superadmin_password"]').should('exist');
    cy.get('input[id="username"]').should('exist');
    cy.get('input[id="password"]').should('exist');
    cy.get('input[id="confirm_password"]').should('exist');
    cy.get('button[type="submit"]').should('contain', 'Créer le Premier Administrateur');
  });

  it('Doit créer un administrateur avec succès (ST-008)', () => {
    cy.visit('/superadmin');
    cy.get('input[id="superadmin_password"]').type('Citron6-Mustang9');
    cy.get('input[id="username"]').type('admin');
    cy.get('input[id="password"]').type('MonMotDePasse123!');
    cy.get('input[id="confirm_password"]').type('MonMotDePasse123!');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/auth/login');
  });

  it('Doit afficher une erreur si le mot de passe superadmin est incorrect (ST-008)', () => {
    cy.visit('/superadmin');
    cy.get('input[id="superadmin_password"]').type('MauvaisMotDePasse');
    cy.get('input[id="username"]').type('admin');
    cy.get('input[id="password"]').type('MonMotDePasse123!');
    cy.get('input[id="confirm_password"]').type('MonMotDePasse123!');
    cy.get('button[type="submit"]').click();
    cy.contains('Mot de passe superadmin incorrect.').should('exist');
  });

  it('Doit afficher une erreur si les mots de passe ne correspondent pas (ST-008)', () => {
    cy.visit('/superadmin');
    cy.get('input[id="superadmin_password"]').type('Citron6-Mustang9');
    cy.get('input[id="username"]').type('admin');
    cy.get('input[id="password"]').type('MotDePasse1');
    cy.get('input[id="confirm_password"]').type('MotDePasse2');
    cy.get('button[type="submit"]').click();
    cy.contains('Les mots de passe ne correspondent pas.').should('exist');
  });

  afterEach(() => {
    if (consoleErrors.length > 0) {
      cy.writeFile('reports/ST-008-console-errors.json', consoleErrors);
    }
  });
});