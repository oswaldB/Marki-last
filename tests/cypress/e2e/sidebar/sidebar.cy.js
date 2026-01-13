// tests/cypress/e2e/sidebar/sidebar.cy.js
describe('Sidebar', () => {
  beforeEach(() => {
    cy.login('user');
    cy.visit('/');
  });

  it('ST-006: Doit afficher la sidebar', () => {
    cy.get('[data-testid="sidebar"]').should('be.visible');
    cy.get('[data-testid="nav-links"]').should('be.visible');
  });

  it('ST-006: Doit basculer la sidebar sur mobile', () => {
    cy.viewport('iphone-6');
    cy.get('[data-testid="sidebar"]').should('not.be.visible');
    cy.get('[data-testid="sidebar-toggle"]').click();
    cy.get('[data-testid="sidebar"]').should('be.visible');
  });

  it('ST-006: Doit mettre à jour les liens de navigation', () => {
    cy.intercept('GET', '/api/nav-links', { fixture: 'nav_links_updated.json' }).as('getNavLinks');
    cy.reload();
    cy.wait('@getNavLinks');
    cy.get('[data-testid="nav-links"]').should('contain', 'Updated Link');
  });
});