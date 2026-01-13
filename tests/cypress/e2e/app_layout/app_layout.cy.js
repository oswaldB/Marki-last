// tests/cypress/e2e/app_layout/app_layout.cy.js
describe('App Layout', () => {
  beforeEach(() => {
    cy.login('user');
    cy.visit('/');
  });

  it('ST-001: Doit afficher le layout principal', () => {
    cy.get('[data-testid="sidebar"]').should('be.visible');
    cy.get('[data-testid="topbar"]').should('be.visible');
    cy.get('[data-testid="content"]').should('be.visible');
  });

  it('ST-001: Doit être responsive sur mobile', () => {
    cy.viewport('iphone-6');
    cy.get('[data-testid="sidebar"]').should('not.be.visible');
    cy.get('[data-testid="topbar"]').should('be.visible');
  });

  it('ST-001: Doit mettre à jour les informations utilisateur', () => {
    cy.intercept('GET', '/api/user', { fixture: 'user_updated.json' }).as('getUser');
    cy.reload();
    cy.wait('@getUser');
    cy.get('[data-testid="user-info"]').should('contain', 'Updated User');
  });
});