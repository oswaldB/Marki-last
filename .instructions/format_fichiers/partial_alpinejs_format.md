# Format des Fichiers de Partial Alpine.js

Ce document définit le format et les conventions pour les fichiers de spécifications des partials Alpine.js dans le dossier `specs/_app/templates/` du projet Marki.

---

## 📂 Structure des Dossiers

Les fichiers de spécifications des partials Alpine.js doivent être organisés selon la structure suivante :

```bash
specs/
└── _app/
    └── templates/
        ├── <nom_du_partial>.html.spec  # Spécifications techniques du partial
        └── ...
```

**Exemple** :
- Spécifications d'un partial : `specs/_app/templates/login_form.html.spec`

---

## 📄 Format du Fichier

### Nom du Fichier

Les fichiers de spécifications des partials Alpine.js doivent être nommés selon le format suivant :
- `<nom_du_partial>.html.spec`

**Exemple** :
- `login_form.html.spec`

### Contenu du Fichier

Chaque fichier de spécifications d'un partial Alpine.js doit contenir les sections suivantes :

#### 1. **En-tête**
```markdown
# Partial: <Nom du Partial>
**Fichier miroir** : `app/templates/partials/<nom_du_partial>.html`
**Description** : <Description courte du partial.>
**Date de création** : <YYYY-MM-DD>
**Auteur** : <Nom de l'auteur>
```

**Exemple** :
```markdown
# Partial: LoginForm
**Fichier miroir** : `app/templates/partials/login_form.html`
**Description** : Formulaire de connexion avec validation.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard
```

#### 2. **Structure HTML**
Cette section doit décrire la structure HTML du partial sans inclure le code HTML. Les classes utilisées sont celles de Tailwind CSS.

```markdown
## 📄 Structure HTML

- **Container** : `<div>` avec les classes Tailwind `<classes>` et les attributs `<attributs>`.
  - **Logo** : `<img>` avec la source `<source>` et les classes Tailwind `<classes>`.
  - **Form** : `<form>` avec les classes Tailwind `<classes>`.
    - **Email Input** : `<input>` avec les attributs `<attributs>` et les classes Tailwind `<classes>`.
    - **Password Input** : `<input>` avec les attributs `<attributs>` et les classes Tailwind `<classes>`.
    - **Submit Button** : `<button>` avec les classes Tailwind `<classes>` et les attributs `<attributs>`.
  - **Error Message** : `<div>` avec les classes Tailwind `<classes>` et les attributs `<attributs>`.
```

**Exemple** :
```markdown
## 📄 Structure HTML

- **Container** : `<div>` avec les classes Tailwind `container mx-auto p-4` et les attributs `x-data="LoginForm()"`.
  - **Logo** : `<img>` avec la source `/static/images/marki-logo.png` et les classes Tailwind `w-20 h-20 mx-auto`.
  - **Form** : `<form>` avec les classes Tailwind `space-y-4`.
    - **Email Input** : `<input>` avec les attributs `x-model="email"`, `type="email"`, `placeholder="Email"`, et les classes Tailwind `w-full p-2 border rounded`.
    - **Password Input** : `<input>` avec les attributs `x-model="password"`, `type="password"`, `placeholder="Mot de passe"`, et les classes Tailwind `w-full p-2 border rounded`.
    - **Submit Button** : `<button>` avec les classes Tailwind `bg-blue-500 text-white p-2 rounded` et les attributs `@click="submit()"`.
  - **Error Message** : `<div>` avec les classes Tailwind `text-red-500` et les attributs `x-text="errorMessage"`.
```

#### 3. **Composant Alpine.js**
Cette section doit décrire la structure de la fonction `ComponentState()` en utilisant le format JSDoc.

```markdown
## 🎨 Composant Alpine.js

### `ComponentState()`

**Description** :
<Description du composant.>

**Propriétés** :
| Nom           | Type   | Description                          | Exemple          |
|---------------|--------|--------------------------------------|------------------|
| <prop1>       | <type> | <description>                        | <exemple>        |
| <prop2>       | <type> | <description>                        | <exemple>        |

**Méthodes** :

#### `<Nom de la Méthode>`
**Description** :
<Description de la méthode.>

**Paramètres** :
| Nom       | Type   | Description                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| <param1>  | <type> | <description>                  | <exemple>        |
| <param2>  | <type> | <description>                  | <exemple>        |

**Retour** :
<Description du retour.>

**Exemple d'utilisation** :
```javascript
this.<nom_de_la_methode>(<param1>, <param2>);
```

**Code** :
```javascript
function ComponentState() {
    return {
        <prop1>: <valeur>,
        <prop2>: <valeur>,
        <nom_de_la_methode>(<param1>, <param2>) {
            // Logique de la méthode
        }
    };
}
```
```

**Exemple** :
```markdown
## 🎨 Composant Alpine.js

### `LoginForm()`

**Description** :
Gère l'état et les interactions du formulaire de connexion.

**Propriétés** :
| Nom           | Type   | Description                          | Exemple          |
|---------------|--------|--------------------------------------|------------------|
| email         | str    | Email de l'utilisateur               | test@example.com |
| password      | str    | Mot de passe de l'utilisateur        | Secure123        |
| errorMessage  | str    | Message d'erreur à afficher          | "Email invalide"|

**Méthodes** :

#### `validateEmail()`
**Description** :
Valide le format de l'email.

**Paramètres** :
Aucun.

**Retour** :
`True` si l'email est valide, `False` sinon.

**Exemple d'utilisation** :
```javascript
this.validateEmail();
```

**Code** :
```javascript
validateEmail() {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(this.email);
}
```

#### `validatePassword()`
**Description** :
Valide le format du mot de passe.

**Paramètres** :
Aucun.

**Retour** :
`True` si le mot de passe est valide, `False` sinon.

**Exemple d'utilisation** :
```javascript
this.validatePassword();
```

**Code** :
```javascript
validatePassword() {
    return this.password.length >= 8;
}
```

#### `submit()`
**Description** :
Soumet le formulaire de connexion.

**Paramètres** :
Aucun.

**Retour** :
Aucun.

**Exemple d'utilisation** :
```javascript
this.submit();
```

**Code** :
```javascript
submit() {
    if (!this.validateEmail() || !this.validatePassword()) {
        this.errorMessage = "Email ou mot de passe invalide.";
        return;
    }
    // Logique de soumission
}
```
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

### Fichier : `specs/_app/templates/login_form.html.spec`
```markdown
# Partial: LoginForm
**Fichier miroir** : `app/templates/partials/login_form.html`
**Description** : Formulaire de connexion avec validation.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard

---

## 📄 Structure HTML

- **Container** : `<div>` avec les classes `marki-form` et les attributs `x-data="LoginForm()"`.
  - **Logo** : `<img>` avec la source `/static/images/marki-logo.png` et les classes `marki-logo`.
  - **Form** : `<form>` avec les classes `marki-input-group`.
    - **Email Input** : `<input>` avec les attributs `x-model="email"`, `type="email"`, et `placeholder="Email"`.
    - **Password Input** : `<input>` avec les attributs `x-model="password"`, `type="password"`, et `placeholder="Mot de passe"`.
    - **Submit Button** : `<button>` avec les classes `marki-button` et les attributs `@click="submit()"`.
  - **Error Message** : `<div>` avec les classes `marki-error` et les attributs `x-text="errorMessage"`.

---

## 🎨 Composant Alpine.js

### `LoginForm()`

**Description** :
Gère l'état et les interactions du formulaire de connexion.

**Propriétés** :
| Nom           | Type   | Description                          | Exemple          |
|---------------|--------|--------------------------------------|------------------|
| email         | str    | Email de l'utilisateur               | test@example.com |
| password      | str    | Mot de passe de l'utilisateur        | Secure123        |
| errorMessage  | str    | Message d'erreur à afficher          | "Email invalide"|

**Méthodes** :

#### `validateEmail()`
**Description** :
Valide le format de l'email.

**Paramètres** :
Aucun.

**Retour** :
`True` si l'email est valide, `False` sinon.

**Exemple d'utilisation** :
```javascript
this.validateEmail();
```

**Code** :
```javascript
validateEmail() {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(this.email);
}
```

#### `validatePassword()`
**Description** :
Valide le format du mot de passe.

**Paramètres** :
Aucun.

**Retour** :
`True` si le mot de passe est valide, `False` sinon.

**Exemple d'utilisation** :
```javascript
this.validatePassword();
```

**Code** :
```javascript
validatePassword() {
    return this.password.length >= 8;
}
```

#### `submit()`
**Description** :
Soumet le formulaire de connexion.

**Paramètres** :
Aucun.

**Retour** :
Aucun.

**Exemple d'utilisation** :
```javascript
this.submit();
```

**Code** :
```javascript
submit() {
    if (!this.validateEmail() || !this.validatePassword()) {
        this.errorMessage = "Email ou mot de passe invalide.";
        return;
    }
    // Logique de soumission
}
```
```

---

## 📌 Notes Supplémentaires

- Les spécifications techniques doivent être synchronisées avec les fichiers de spécifications dans `specs/specs/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
