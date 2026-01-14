describe('ST-002: Hello World Page', () => {
  const consoleErrors = [];

  beforeEach(() => {
    // Capture console errors
    cy.on('window:console', (str, args) => {
      if (str === 'error' || str === 'warn') {
        consoleErrors.push({
          type: str,
          message: args[0],
          stack: args[1] ? args[1].stack : undefined,
        });
      }
    });

    cy.on('uncaught:exception', (err) => {
      consoleErrors.push({
        name: err.name,
        message: err.message,
        stack: err.stack,
      });
      return false;
    });

    cy.visit('/hello');
  });

  afterEach(() => {
    // Check for network errors
    cy.window().then((win) => {
      const performanceEntries = win.performance.getEntries();
      const networkErrors = performanceEntries.filter((entry) => {
        return entry.initiatorType === 'img' && entry.responseStatus === 404;
      });

      if (networkErrors.length > 0) {
        const errors = networkErrors.map((entry) => ({
          type: 'network',
          url: entry.name,
          status: entry.responseStatus,
          message: `Failed to load resource: the server responded with a status of ${entry.responseStatus} (NOT FOUND)`,
        }));
        cy.writeFile('reports/ST-002-console-errors.json', errors);
      }

      if (consoleErrors.length > 0) {
        cy.writeFile('reports/ST-002-console-errors.json', consoleErrors);
      }
    });
  });

  it('ST-002: Should display the logo', () => {
    cy.get('img.logo').should('be.visible');
    cy.get('img.logo').invoke('attr', 'src').should('include', '/static/logo.png');
    cy.get('img.logo').should('have.attr', 'alt', 'Logo Marki');
  });

  it('ST-002: Should display the welcome message', () => {
    cy.get('.message').should('be.visible');
    cy.get('.message').should('contain.text', 'Hello, World!');
  });

  it('ST-002: Should have correct logo styles', () => {
    cy.get('img.logo').should('have.css', 'max-width', '200px');
    cy.get('img.logo').should('have.css', 'margin-bottom', '20px');
  });

  it('ST-002: Should have correct message styles', () => {
    cy.get('.message').should('have.css', 'font-size', '24px');
    cy.get('body').should('have.css', 'text-align', 'center');
  });

  it('ST-002: Should have correct page title', () => {
    cy.title().should('include', 'Hello World - Marki');
  });

  it('ST-002: Should have correct body styles', () => {
    cy.get('body').should('have.css', 'margin-top', '50px');
    cy.get('body').should('have.css', 'color', 'rgb(51, 51, 51)');
  });

  it('ST-002: Should have correct font family', () => {
    cy.get('body').should('have.css', 'font-family', 'Inter, sans-serif');
  });

  it('ST-002: Should have correct message color', () => {
    cy.get('.message').should('have.css', 'color', 'rgb(51, 51, 51)');
  });

  it('ST-002: Should be responsive', () => {
    cy.viewport(320, 480);
    cy.get('img.logo').should('be.visible');
    cy.get('.message').should('be.visible');
    cy.get('body').should('have.css', 'text-align', 'center');

    cy.viewport(1280, 720);
    cy.get('img.logo').should('be.visible');
    cy.get('.message').should('be.visible');
    cy.get('body').should('have.css', 'text-align', 'center');
  });
});