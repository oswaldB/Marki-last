# Format des Fichiers de Tests Playwright

Ce document définit le format et les conventions pour les fichiers de tests Playwright dans le dossier `tests/` du projet Marki.

---

## 📂 Structure des Dossiers

Les fichiers de tests Playwright doivent être organisés dans le dossier `tests/` selon la structure suivante :

```bash
tests/
├── <nom_du_test>.spec.ts  # Fichier de test Playwright
└── fixtures/              # Données de test (si nécessaire)
    └── <nom_du_fixture>.json
```

**Exemple** :
- Test : `tests/ST-008_inscription.spec.ts`
- Fixture : `tests/fixtures/users.json`

---

## 📄 Format du Fichier

### Nom du Fichier

Les fichiers de tests Playwright doivent être nommés selon le format suivant :
- `ST-<NUM>_<nom_du_test>.spec.ts`

**Exemple** :
- `ST-008_inscription.spec.ts`
- `ST-001_hello_world.spec.ts`

### Contenu du Fichier

Chaque fichier de test Playwright doit contenir les sections suivantes :

#### 1. **Importations**
Cette section doit importer les modules nécessaires pour les tests.

```typescript
import { test, expect } from '@playwright/test';
```

**Exemple** :
```typescript
import { test, expect } from '@playwright/test';
```

#### 2. **Description du Test**
Cette section doit décrire le groupe de tests et les tests individuels.

```typescript
test.describe('<Description du groupe de tests>', () => {
  // Tests individuels
});
```

**Exemple** :
```typescript
test.describe('Inscription', () => {
  // Tests individuels
});
```

#### 3. **Configuration avant chaque test**
Cette section doit configurer l'environnement avant chaque test, y compris l'enregistrement des consoles web et serveur. Utilisez le script `capture_console_logs.py` pour capturer et traiter les logs.

```typescript
test.beforeEach(async ({ page }) => {
  await page.goto('<URL_de_la_page>');
  
  // Enregistrement des logs de la console web
  page.on('console', msg => {
    console.log(`Console Web: ${msg.text()}`);
  });
  
  // Enregistrement des logs de la console serveur (si applicable)
  page.on('request', request => {
    console.log(`Request: ${request.method()} ${request.url()}`);
  });
  
  page.on('response', response => {
    console.log(`Response: ${response.status()} ${response.url()}`);
  });
  
  page.on('requestfailed', request => {
    console.log(`Request Failed: ${request.failure().errorText}`);
  });
});
```

**Exemple** :
```typescript
test.beforeEach(async ({ page }) => {
  await page.goto('/inscription');
  
  // Enregistrement des logs de la console web
  page.on('console', msg => {
    console.log(`Console Web: ${msg.text()}`);
  });
  
  // Enregistrement des logs de la console serveur (si applicable)
  page.on('request', request => {
    console.log(`Request: ${request.method()} ${request.url()}`);
  });
  
  page.on('response', response => {
    console.log(`Response: ${response.status()} ${response.url()}`);
  });
  
  page.on('requestfailed', request => {
    console.log(`Request Failed: ${request.failure().errorText}`);
  });
});
```

**Utilisation du script `capture_console_logs.py`** :

Pour capturer et traiter les logs des tests, utilisez le script `capture_console_logs.py` situé à la racine du projet. Ce script permet de capturer les logs de la console web et serveur, et de les enregistrer dans un fichier JSON pour une analyse ultérieure.

**Exemple d'utilisation** :

1. **Exécuter les tests Playwright** :
```bash
npx playwright test
```

2. **Capturer les logs** :
```bash
python capture_console_logs.py
```

3. **Analyser les logs** :
Les logs capturés seront enregistrés dans le fichier `console_logs.json` à la racine du projet. Vous pouvez analyser ce fichier pour identifier les erreurs et les problèmes.

**Exemple de contenu du fichier `console_logs.json`** :
```json
{
  "logs": [
    {
      "type": "console",
      "message": "Console Web: Email invalide",
      "timestamp": "2026-01-20T12:00:00.000Z"
    },
    {
      "type": "request",
      "method": "POST",
      "url": "/api/login",
      "timestamp": "2026-01-20T12:00:01.000Z"
    },
    {
      "type": "response",
      "status": 200,
      "url": "/api/login",
      "timestamp": "2026-01-20T12:00:02.000Z"
    }
  ]
}
```

#### 4. **Tests Individuels**
Cette section doit contenir les tests individuels avec leurs descriptions et leurs assertions.

```typescript
test('<Description du test>', async ({ page }) => {
  // Actions
  await page.fill('<sélecteur>', '<valeur>');
  await page.click('<sélecteur>');
  
  // Assertions
  await expect(page.locator('<sélecteur>')).toBeVisible();
  await expect(page).toHaveURL('<URL_attendue>');
});
```

**Exemple** :
```typescript
test('Doit afficher une erreur si email invalide', async ({ page }) => {
  await page.fill('input[type="email"]', 'invalid');
  await page.click('button[type="submit"]');
  await expect(page.locator('text=Email invalide')).toBeVisible();
});

test('Doit rediriger vers /success si inscription valide', async ({ page }) => {
  await page.fill('input[type="email"]', 'test@example.com');
  await page.fill('input[type="password"]', 'Secure123');
  await page.fill('input[type="text"]', 'Test User');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/success');
});
```

#### 5. **Utilisation des Fixtures**
Cette section doit décrire comment utiliser les fixtures pour les données de test.

```typescript
import users from '../fixtures/users.json';

test('Doit afficher les utilisateurs', async ({ page }) => {
  for (const user of users) {
    await page.fill('input[type="email"]', user.email);
    await page.fill('input[type="password"]', user.password);
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Utilisateur connecté')).toBeVisible();
  }
});
```

**Exemple** :
```typescript
import users from '../fixtures/users.json';

test('Doit afficher les utilisateurs', async ({ page }) => {
  for (const user of users) {
    await page.fill('input[type="email"]', user.email);
    await page.fill('input[type="password"]', user.password);
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Utilisateur connecté')).toBeVisible();
  }
});
```

---

## 📝 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises pour les tests.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Isolation** : Chaque test doit être indépendant et ne pas dépendre des autres tests.
4. **Assertions** : Utilisez des assertions claires pour vérifier les résultats attendus.
5. **Fixtures** : Utilisez des fixtures pour les données de test réutilisables.
6. **Documentation** : Documentez les tests pour faciliter la maintenance.

---

## 📌 Exemple Complet

### Fichier : `tests/ST-008_inscription.spec.ts`
```typescript
import { test, expect } from '@playwright/test';

// Configuration avant chaque test
test.beforeEach(async ({ page }) => {
  await page.goto('/inscription');
  
  // Enregistrement des logs de la console web
  page.on('console', msg => {
    console.log(`Console Web: ${msg.text()}`);
  });
  
  // Enregistrement des logs de la console serveur (si applicable)
  page.on('request', request => {
    console.log(`Request: ${request.method()} ${request.url()}`);
  });
  
  page.on('response', response => {
    console.log(`Response: ${response.status()} ${response.url()}`);
  });
  
  page.on('requestfailed', request => {
    console.log(`Request Failed: ${request.failure().errorText}`);
  });
});

// Tests pour l'inscription
test.describe('Inscription', () => {
  test('Doit afficher une erreur si email invalide', async ({ page }) => {
    await page.fill('input[type="email"]', 'invalid');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Email invalide')).toBeVisible();
  });

  test('Doit afficher une erreur si mot de passe trop court', async ({ page }) => {
    await page.fill('input[type="email"]', 'test@example.com');
    await page.fill('input[type="password"]', 'short');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Mot de passe trop court')).toBeVisible();
  });

  test('Doit rediriger vers /success si inscription valide', async ({ page }) => {
    await page.fill('input[type="email"]', 'test@example.com');
    await page.fill('input[type="password"]', 'Secure123');
    await page.fill('input[type="text"]', 'Test User');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL('/success');
  });
});
```

### Fichier : `capture_console_logs.py`

Ce script est utilisé pour capturer et traiter les logs des tests Playwright. Il est situé à la racine du projet et peut être exécuté après les tests pour analyser les logs.

**Exemple d'utilisation** :

1. **Exécuter les tests Playwright** :
```bash
npx playwright test
```

2. **Capturer les logs** :
```bash
python capture_console_logs.py
```

3. **Analyser les logs** :
Les logs capturés seront enregistrés dans le fichier `console_logs.json` à la racine du projet. Vous pouvez analyser ce fichier pour identifier les erreurs et les problèmes.

**Exemple de contenu du fichier `console_logs.json`** :
```json
{
  "logs": [
    {
      "type": "console",
      "message": "Console Web: Email invalide",
      "timestamp": "2026-01-20T12:00:00.000Z"
    },
    {
      "type": "request",
      "method": "POST",
      "url": "/api/login",
      "timestamp": "2026-01-20T12:00:01.000Z"
    },
    {
      "type": "response",
      "status": 200,
      "url": "/api/login",
      "timestamp": "2026-01-20T12:00:02.000Z"
    }
  ]
}
```

### Fichier : `tests/fixtures/users.json`
```json
[
  {
    "email": "test1@example.com",
    "password": "Secure123",
    "name": "Test User 1"
  },
  {
    "email": "test2@example.com",
    "password": "Secure456",
    "name": "Test User 2"
  }
]
```

---

## 📌 Notes Supplémentaires

- Les tests Playwright doivent être synchronisés avec les spécifications techniques dans `specs/specs/` et `specs/_app/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
- Utilisez des sélecteurs clairs et spécifiques pour éviter les erreurs de sélection.
