# Partial : Bouton de Déconnexion (ST-010)
**Fichier cible** : `app/templates/partials/topbar.html`

---

## **Description**
Bouton de déconnexion intégré dans le menu utilisateur de la topbar. Permet à l'utilisateur de mettre fin à sa session et d'être redirigé vers la page de login.

---

## **Structure HTML**

Le bouton de déconnexion est intégré dans le menu déroulant utilisateur de la topbar :

```html
<!-- User Dropdown Menu -->
<div class="absolute right-0 mt-2 w-48 bg-white border border-border rounded-lg shadow-lg z-50"
     x-show="showUserMenu" @click.away="showUserMenu = false">
  <div class="p-4 border-b border-border">
    <p class="text-sm font-semibold text-text" x-text="user.username"></p>
    <p class="text-xs text-text-light" x-text="user.email"></p>
  </div>
  <ul class="divide-y divide-border">
    <li>
      <a href="/profile" class="block px-4 py-3 text-sm text-text hover:bg-bg-light transition-colors">
        Mon Profil
      </a>
    </li>
    <li x-show="user.isAdmin">
      <a href="/settings/team" class="block px-4 py-3 text-sm text-text hover:bg-bg-light transition-colors">
        Équipe
      </a>
    </li>
    <li>
      <form action="/auth/logout" method="POST" class="block">
        <button type="submit" class="w-full text-left px-4 py-3 text-sm text-error hover:bg-bg-light transition-colors">
          Déconnexion
        </button>
      </form>
    </li>
  </ul>
</div>
```

---

## **Comportement**

### **1. Affichage**
- Le bouton de déconnexion est visible uniquement lorsque le menu utilisateur est ouvert (`showUserMenu = true`).
- Le bouton est stylisé avec une couleur d'erreur (`text-error`) pour indiquer une action destructive.
- Le bouton est aligné à gauche comme les autres éléments du menu pour une cohérence visuelle.

### **2. Interaction**
- Lorsque l'utilisateur clique sur le bouton, un formulaire est soumis avec la méthode POST vers `/auth/logout`.
- La déconnexion est immédiate et ne nécessite pas de confirmation supplémentaire.
- Après la déconnexion, l'utilisateur est redirigé vers la page de login (`/login`).

### **3. État**
- Le bouton utilise l'état `user` partagé avec le composant parent pour afficher le nom d'utilisateur et l'email.
- Le bouton est toujours visible dans le menu utilisateur, indépendamment des permissions de l'utilisateur.

---

## **Règles Métier**

1. **Visibilité** : Le bouton de déconnexion doit être visible uniquement pour les utilisateurs connectés.
2. **Action** : La déconnexion doit être immédiate et ne pas nécessiter de confirmation supplémentaire.
3. **Redirection** : Après déconnexion, l'utilisateur doit être redirigé vers `/login`.
4. **Sécurité** : La déconnexion doit être effectuée via une requête POST pour éviter les attaques CSRF.

---

## **Liens**

- [Spécifications fonctionnelles](../../specs/ST-010_logout-functionnelles.md)
- [Spécifications des routes d'authentification](../../blueprints/auth/auth.routes.spec.md)
- [Spécifications de la topbar](../../templates/partials/ST-007_topbar.html.spec.md)