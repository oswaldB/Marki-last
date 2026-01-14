# ST-003 : Page de Login - Spécifications Fonctionnelles
**Date** : 2026-01-14
**Auteur** : Specificator
**Statut** : En cours

---

## Contexte
La page de login permet aux utilisateurs authentifiés d'accéder à l'application. Elle doit gérer l'authentification, les erreurs de connexion, et rediriger les utilisateurs vers le tableau de bord après une connexion réussie.

## Acteurs
- **Utilisateur** : Saisit ses identifiants pour se connecter.
- **Administrateur** : Peut accéder à des fonctionnalités supplémentaires après connexion.

## Flux Principal
1. L'utilisateur accède à la page de login via l'URL `/login`.
2. L'utilisateur saisit son identifiant et son mot de passe.
3. Le formulaire est soumis et les identifiants sont validés.
4. Si les identifiants sont valides, l'utilisateur est redirigé vers le tableau de bord (`/dashboard`).
5. Si les identifiants sont invalides, un message d'erreur est affiché.

## Règles Métier
- L'identifiant doit être un identifiant valide (ex: `utilisateur123`).
- Le mot de passe doit contenir au moins 8 caractères.
- Les champs identifiant et mot de passe sont obligatoires.
- Après 3 tentatives infructueuses, le compte est temporairement bloqué pendant 5 minutes.

## Données
- **Entrée** : Identifiant et mot de passe saisis par l'utilisateur.
- **Sortie** : Redirection vers `/dashboard` en cas de succès, ou message d'erreur en cas d'échec.

## Liens
- [Spécifications techniques](../../_app/templates/login.html.spec.md)
- [Spécifications des routes](../../_app/blueprints/auth/auth.routes.spec.md)
- [Spécifications des modèles](../../_app/blueprints/auth/auth.models.spec.md)
