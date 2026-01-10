describe('Hello World Page', () => {
  it('should display hello world page', () => {
    cy.visit('/hello');
    cy.contains('Hello World').should('be.visible');
    cy.contains('Bienvenue sur Marki').should('be.visible');
    cy.contains('Ceci est une page de démonstration').should('be.visible');
    cy.contains('Retour à l\'accueil').should('be.visible');
  });

  it('should have working back button', () => {
    cy.visit('/hello');
    cy.contains('Retour à l\'accueil').click();
    cy.url().should('eq', Cypress.config().baseUrl + '/');
  });
});