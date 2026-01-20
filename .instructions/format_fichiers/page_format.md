# Format des Fichiers de Page

Ce document définit le format et les conventions pour les fichiers de spécifications des pages dans le dossier `specs/_app/templates/` du projet Marki.

---

## 📂 Structure des Dossiers

Les fichiers de spécifications des pages doivent être organisés selon la structure suivante :

```bash
specs/
└── _app/
    └── templates/
        ├── <nom_de_la_page>.html.spec  # Spécifications techniques de la page
        └── ...
```

**Exemple** :
- Spécifications d'une page : `specs/_app/templates/login.html.spec`

---

## 📄 Format du Fichier

### Nom du Fichier

Les fichiers de spécifications des pages doivent être nommés selon le format suivant :
- `<nom_de_la_page>.html.spec`

**Exemple** :
- `login.html.spec`

### Contenu du Fichier

Chaque fichier de spécifications d'une page doit contenir les sections suivantes :

#### 1. **En-tête**
```markdown
# Page: <Nom de la Page>
**Fichier miroir** : `app/templates/<nom_de_la_page>.html`
**Description** : <Description courte de la page.>
**Date de création** : <YYYY-MM-DD>
**Auteur** : <Nom de l'auteur>
```

**Exemple** :
```markdown
# Page: Login
**Fichier miroir** : `app/templates/login.html`
**Description** : Page de connexion des utilisateurs.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard
```

#### 2. **Structure HTML**
Cette section doit décrire la structure HTML de la page sans inclure le code HTML.

```markdown
## 📄 Structure HTML

- **Layout** : `<layout>` avec le nom `<nom_du_layout>`.
  - **Title** : `<title>` avec le texte `<texte>`.
  - **Meta** : `<meta>` avec les attributs `<attributs>`.
  - **Link** : `<link>` avec les attributs `<attributs>`.
  - **Body** : `<body>` avec les classes `<classes>`.
    - **Header** : `<header>` avec les classes `<classes>`.
      - **Logo** : `<img>` avec la source `<source>` et les classes `<classes>`.
      - **Navigation** : `<nav>` avec les classes `<classes>`.
        - **Link** : `<a>` avec le texte `<texte>` et les attributs `<attributs>`.
    - **Main** : `<main>` avec les classes `<classes>`.
      - **Section** : `<section>` avec les classes `<classes>`.
        - **Partial** : `<partial>` avec le nom `<nom_du_partial>`.
    - **Footer** : `<footer>` avec les classes `<classes>`.
      - **Copyright** : `<p>` avec le texte `<texte>`.
```

**Exemple** :
```markdown
## 📄 Structure HTML

- **Layout** : `<layout>` avec le nom `base.html`.
  - **Title** : `<title>` avec le texte `Login - Marki`.
  - **Meta** : `<meta>` avec les attributs `charset="UTF-8"` et `name="viewport" content="width=device-width, initial-scale=1.0"`.
  - **Link** : `<link>` avec les attributs `rel="stylesheet"` et `href="/static/css/styles.css"`.
  - **Body** : `<body>` avec les classes `marki-body`.
    - **Header** : `<header>` avec les classes `marki-header`.
      - **Logo** : `<img>` avec la source `/static/images/marki-logo.png` et les classes `marki-logo`.
      - **Navigation** : `<nav>` avec les classes `marki-nav`.
        - **Link** : `<a>` avec le texte `Accueil` et les attributs `href="/"`.
        - **Link** : `<a>` avec le texte `Inscription` et les attributs `href="/register"`.
    - **Main** : `<main>` avec les classes `marki-main`.
      - **Section** : `<section>` avec les classes `marki-section`.
        - **Partial** : `<partial>` avec le nom `login_form.html`.
    - **Footer** : `<footer>` avec les classes `marki-footer`.
      - **Copyright** : `<p>` avec le texte `© 2026 Marki. Tous droits réservés.`.
```

#### 3. **Partials**
Cette section doit lister les partials utilisés dans la page.

```markdown
## 🧩 Partials

| Nom du Partial       | Description                          | Chemin du Partial                     |
|----------------------|--------------------------------------|---------------------------------------|
| <nom_du_partial>     | <description>                        | `app/templates/partials/<nom>.html`   |
| <nom_du_partial>     | <description>                        | `app/templates/partials/<nom>.html`   |
```

**Exemple** :
```markdown
## 🧩 Partials

| Nom du Partial       | Description                          | Chemin du Partial                     |
|----------------------|--------------------------------------|---------------------------------------|
| login_form.html      | Formulaire de connexion              | `app/templates/partials/login_form.html`|
| header.html          | En-tête de la page                   | `app/templates/partials/header.html`   |
| footer.html          | Pied de page                         | `app/templates/partials/footer.html`   |
```

#### 4. **Scripts**
Cette section doit décrire les scripts utilisés dans la page.

```markdown
## 📜 Scripts

| Nom du Script       | Description                          | Chemin du Script                     |
|---------------------|--------------------------------------|---------------------------------------|
| <nom_du_script>     | <description>                        | `<chemin_du_script>`                  |
| <nom_du_script>     | <description>                        | `<chemin_du_script>`                  |
```

**Exemple** :
```markdown
## 📜 Scripts

| Nom du Script       | Description                          | Chemin du Script                     |
|---------------------|--------------------------------------|---------------------------------------|
| login.js            | Logique de la page de connexion      | `app/static/js/login.js`              |
| alpine.js           | Bibliothèque Alpine.js                | `https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js`|
```

#### 5. **Styles**
Cette section doit décrire les styles utilisés dans la page. Comme nous utilisons Tailwind CSS en CDN, il n'y a pas de fichiers CSS spécifiques à lister.

```markdown
## 🎨 Styles

- **Tailwind CSS** : Utilisé via CDN pour les styles globaux et spécifiques.
  - **CDN** : `https://cdn.jsdelivr.net/npm/tailwindcss@3.x.x/dist/tailwind.min.css`
```

**Exemple** :
```markdown
## 🎨 Styles

- **Tailwind CSS** : Utilisé via CDN pour les styles globaux et spécifiques.
  - **CDN** : `https://cdn.jsdelivr.net/npm/tailwindcss@3.x.x/dist/tailwind.min.css`
```

---

## 📝 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Exemples** : Fournissez des exemples pour illustrer les spécifications.
4. **Mises à Jour** : Documentez toute mise à jour ou modification.
5. **Validation** : Assurez-vous que les spécifications sont validées par l'équipe avant d'être fusionnées.

---

## 📌 Exemple Complet

### Fichier : `specs/_app/templates/login.html.spec`
```markdown
# Page: Login
**Fichier miroir** : `app/templates/login.html`
**Description** : Page de connexion des utilisateurs.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard

---

## 📄 Structure HTML

- **Layout** : `<layout>` avec le nom `base.html`.
  - **Title** : `<title>` avec le texte `Login - Marki`.
  - **Meta** : `<meta>` avec les attributs `charset="UTF-8"` et `name="viewport" content="width=device-width, initial-scale=1.0"`.
  - **Link** : `<link>` avec les attributs `rel="stylesheet"` et `href="/static/css/styles.css"`.
  - **Body** : `<body>` avec les classes `marki-body`.
    - **Header** : `<header>` avec les classes `marki-header`.
      - **Logo** : `<img>` avec la source `/static/images/marki-logo.png` et les classes `marki-logo`.
      - **Navigation** : `<nav>` avec les classes `marki-nav`.
        - **Link** : `<a>` avec le texte `Accueil` et les attributs `href="/"`.
        - **Link** : `<a>` avec le texte `Inscription` et les attributs `href="/register"`.
    - **Main** : `<main>` avec les classes `marki-main`.
      - **Section** : `<section>` avec les classes `marki-section`.
        - **Partial** : `<partial>` avec le nom `login_form.html`.
    - **Footer** : `<footer>` avec les classes `marki-footer`.
      - **Copyright** : `<p>` avec le texte `© 2026 Marki. Tous droits réservés.`.

---

## 🧩 Partials

| Nom du Partial       | Description                          | Chemin du Partial                     |
|----------------------|--------------------------------------|---------------------------------------|
| login_form.html      | Formulaire de connexion              | `app/templates/partials/login_form.html`|
| header.html          | En-tête de la page                   | `app/templates/partials/header.html`   |
| footer.html          | Pied de page                         | `app/templates/partials/footer.html`   |

---

## 📜 Scripts

| Nom du Script       | Description                          | Chemin du Script                     |
|---------------------|--------------------------------------|---------------------------------------|
| login.js            | Logique de la page de connexion      | `app/static/js/login.js`              |
| alpine.js           | Bibliothèque Alpine.js                | `https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js`|

---

## 🎨 Styles

| Nom du Style        | Description                          | Chemin du Style                      |
|---------------------|--------------------------------------|---------------------------------------|
| styles.css          | Styles globaux                       | `app/static/css/styles.css`           |

```

---

## 📌 Notes Supplémentaires

- Les spécifications techniques doivent être synchronisées avec les fichiers de spécifications dans `specs/specs/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
