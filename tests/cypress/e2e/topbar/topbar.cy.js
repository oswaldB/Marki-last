// tests/cypress/e2e/topbar/topbar.cy.js
describe('Topbar', () => {
  beforeEach(() => {
    cy.login('user');
    cy.visit('/');
  });

  it('ST-007: Doit afficher la topbar', () => {
    cy.get('[data-testid="topbar"]').should('be.visible');
    cy.get('[data-testid="user-info"]').should('be.visible');
  });

  it('ST-007: Doit ouvrir le menu déroulant', () => {
    cy.get('[data-testid="user-avatar"]').click();
    cy.get('[data-testid="dropdown-menu"]').should('be.visible');
  });

  it('ST-007: Doit afficher les notifications', () => {
    cy.get('[data-testid="notification-badge"]').click();
    cy.get('[data-testid="notification-list"]').should('be.visible');
  });
});