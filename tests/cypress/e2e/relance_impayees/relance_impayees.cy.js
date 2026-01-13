// tests/cypress/e2e/relance_impayees/relance_impayees.cy.js
describe('Relance Impayées', () => {
  beforeEach(() => {
    cy.login('user');
    cy.visit('/relances/dashboard');
  });

  it('ST-005: Doit créer une campagne de relance', () => {
    cy.get('[data-testid="create-campaign"]').click();
    cy.get('[data-testid="campaign-name"]').type('Campagne Test');
    cy.get('[data-testid="save-campaign"]').click();
    cy.contains('Campagne créée avec succès').should('be.visible');
  });

  it('ST-005: Doit envoyer des relances', () => {
    cy.intercept('POST', '/api/relances/send', { statusCode: 200 }).as('sendRelances');
    cy.get('[data-testid="send-relances"]').click();
    cy.wait('@sendRelances');
    cy.contains('Relances envoyées').should('be.visible');
  });

  it('ST-005: Doit gérer les erreurs d'envoi', () => {
    cy.intercept('POST', '/api/relances/send', { statusCode: 500 }).as('sendRelancesError');
    cy.get('[data-testid="send-relances"]').click();
    cy.wait('@sendRelancesError');
    cy.contains('Erreur d\'envoi').should('be.visible');
  });
});