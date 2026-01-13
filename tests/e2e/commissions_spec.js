describe('Commissions Valides Page', () => {
  beforeEach(() => {
    cy.visit('/commissions/valides');
  });

  it('should display commissions with conflit status', () => {
    cy.contains('conflit').should('exist');
  });

  it('should display a "Reparer" button for each commission in conflit', () => {
    cy.contains('Reparer').should('exist');
  });

  it('should open repair modal when "Reparer" button is clicked', () => {
    cy.contains('Reparer').first().click();
    cy.contains('Reparer la Commission').should('exist');
  });

  it('should display commissions with valide status', () => {
    cy.contains('valide').should('exist');
  });

  it('should display a table by technician', () => {
    cy.contains('intervenant').should('exist');
  });

  it('should display "Decouper", "Archiver", and "Regler" buttons for each commission', () => {
    cy.contains('Decouper').should('exist');
    cy.contains('Archiver').should('exist');
    cy.contains('Regler').should('exist');
  });

  it('should open subdivide drawer when "Decouper" button is clicked', () => {
    cy.contains('Decouper').first().click();
    cy.contains('Subdiviser la Commission').should('exist');
  });

  it('should filter commissions based on search input', () => {
    cy.get('input[placeholder="Rechercher..."]').type('FACT001');
    cy.contains('FACT001').should('exist');
  });

  it('should close repair modal when "Fermer" button is clicked', () => {
    cy.contains('Reparer').first().click();
    cy.contains('Fermer').click();
    cy.contains('Reparer la Commission').should('not.exist');
  });

  it('should close subdivide drawer when "Fermer" button is clicked', () => {
    cy.contains('Decouper').first().click();
    cy.contains('Fermer').click();
    cy.contains('Subdiviser la Commission').should('not.exist');
  });

  it('should archive a commission when "Archiver" button is clicked', () => {
    cy.contains('Archiver').first().click();
    cy.on('window:alert', (text) => {
      expect(text).to.contains('Commission archivée avec succès');
    });
  });

  it('should settle a commission when "Regler" button is clicked', () => {
    cy.contains('Regler').first().click();
    cy.on('window:alert', (text) => {
      expect(text).to.contains('Commission réglée avec succès');
    });
  });

  it('should subdivide a commission line when "Valider" button is clicked', () => {
    cy.contains('Decouper').first().click();
    cy.get('input[type="number"]').first().type('500');
    cy.get('input[type="number"]').eq(1).type('600');
    cy.contains('Valider').click();
    cy.on('window:alert', (text) => {
      expect(text).to.contains('Ligne subdivisée avec succès');
    });
  });
});

describe('Commissions Conflits Page', () => {
  beforeEach(() => {
    cy.visit('/commissions/conflits');
  });

  it('should display commissions with conflit status', () => {
    cy.contains('conflit').should('exist');
  });

  it('should display a "Reparer" button for each commission in conflit', () => {
    cy.contains('Reparer').should('exist');
  });

  it('should open repair modal when "Reparer" button is clicked', () => {
    cy.contains('Reparer').first().click();
    cy.contains('Reparer la Commission').should('exist');
  });

  it('should close repair modal when "Fermer" button is clicked', () => {
    cy.contains('Reparer').first().click();
    cy.contains('Fermer').click();
    cy.contains('Reparer la Commission').should('not.exist');
  });
});