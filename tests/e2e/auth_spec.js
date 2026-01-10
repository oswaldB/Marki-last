// tests/e2e/auth_spec.js
describe('Authentification', () => {
  it('devrait permettre à un utilisateur de se connecter avec des identifiants valides', () => {
    cy.visit('/auth/login');
    cy.get('input[name="username"]').type('admin');
    cy.get('input[name="password"]').type('admin123');
    cy.get('button[type="submit"]').click();
    cy.contains('Utilisateur connecté avec succès').should('be.visible');
  });

  it('devrait permettre à un utilisateur de demander une réinitialisation de mot de passe', () => {
    cy.visit('/auth/reset_password');
    cy.get('input[name="email"]').type('admin@marki.com');
    cy.get('button[type="submit"]').click();
    cy.contains('Lien de réinitialisation envoyé').should('be.visible');
  });
});