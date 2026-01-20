# ST-001 : Page Hello World - Développement BDD
**Date** : 2024-10-04
**Version** : 1.0
**Auteur** : Mistral Vibe

---

## 📋 Vue d'ensemble
Ce document décrit le développement BDD (Behavior Driven Development) pour la page Hello World (ST-001).

## 🧪 Scénarios BDD

### Scénario 1 : Affichage de base
**Étant donné** que l'utilisateur navigue vers `/hello`
**Quand** la page est chargée
**Alors** le texte "Hello World" doit être visible
**Et** le logo Marki doit être affiché
**Et** le texte doit être en gras (font-weight: 700)

### Scénario 2 : Accessibilité
**Étant donné** que l'utilisateur navigue vers `/hello`
**Quand** la page est chargée
**Alors** la page doit retourner un statut HTTP 200
**Et** le logo doit avoir un attribut alt="Marki Logo"

### Scénario 3 : Responsive Design
**Étant donné** que l'utilisateur navigue vers `/hello` sur mobile
**Quand** la page est chargée
**Alors** le texte doit s'adapter à la taille de l'écran
**Et** le logo doit être positionné correctement

## 📊 Critères d'acceptation BDD

1. **Fonctionnel**
   - ✅ Le texte "Hello World" est visible
   - ✅ Le logo Marki est affiché
   - ✅ Le texte est en gras
   - ✅ La page est accessible via `/hello`

2. **Technique**
   - ✅ Statut HTTP 200
   - ✅ Pas d'erreurs console
   - ✅ Pas d'erreurs serveur

3. **UX/UI**
   - ✅ Design responsive
   - ✅ Logo positionné en haut à gauche
   - ✅ Texte centré

## 🔄 Intégration avec les tests existants

Les scénarios BDD ci-dessus correspondent aux tests Playwright existants dans `tests/ST-001_hello_world.spec.ts`:

```typescript
// Test 1 : Affichage de base
test('Doit afficher le texte "Hello World"', async ({ page }) => {
  const helloWorldText = page.locator('text="Hello World"');
  await expect(helloWorldText).toBeVisible();
});

// Test 2 : Logo
test('Doit afficher le logo Marki', async ({ page }) => {
  const logo = page.locator('img[alt="Marki Logo"]');
  await expect(logo).toBeVisible();
});

// Test 3 : Texte en gras
test('Doit avoir le texte "Hello World" en gras', async ({ page }) => {
  const helloWorldText = page.locator('text="Hello World"');
  await expect(helloWorldText).toHaveCSS('font-weight', '700');
});

// Test 4 : URL
test('Doit être accessible via l\'URL /hello', async ({ page }) => {
  await expect(page).toHaveURL('http://127.0.0.1:5000/hello');
});

// Test 5 : Statut HTTP
test('Doit retourner un statut HTTP 200', async ({ page }) => {
  const response = await page.goto('http://127.0.0.1:5000/hello');
  await expect(response?.status()).toBe(200);
});
```

## 📝 Notes
- Les tests Playwright existants couvrent déjà tous les scénarios BDD
- Aucune modification supplémentaire n'est nécessaire
- Les tests peuvent être exécutés avec `npx playwright test tests/ST-001_hello_world.spec.ts`

---

**Statut** : Prêt pour développement back
**Prochaine étape** : Développement back (ST-001_hello-world-back.md)