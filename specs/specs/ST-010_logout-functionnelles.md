# ST-010 : Bouton de Déconnexion - Spécifications Fonctionnelles
**Date** : 2026-01-15
**Auteur** : Specificator
**Statut** : En cours

---

## Contexte
Le bouton de déconnexion permet aux utilisateurs de mettre fin à leur session active et d'être redirigés vers la page de login. Cette fonctionnalité est essentielle pour la sécurité et la gestion des sessions utilisateur.

## Acteurs
- **Utilisateur** : Clique sur le bouton de déconnexion pour mettre fin à sa session.
- **Système** : Gère la déconnexion et la redirection.

## Flux Principal
1. L'utilisateur est connecté et visualise l'interface de l'application.
2. L'utilisateur clique sur le bouton de déconnexion situé dans la barre supérieure (topbar).
3. Le système met fin à la session utilisateur.
4. L'utilisateur est redirigé vers la page de login (`/login`).
5. L'utilisateur voit un message de confirmation de déconnexion.

## Règles Métier
- Le bouton de déconnexion doit être visible uniquement pour les utilisateurs connectés.
- La déconnexion doit être immédiate et ne pas nécessiter de confirmation supplémentaire.
- Après déconnexion, l'utilisateur ne doit pas pouvoir accéder aux pages protégées sans se reconnecter.
- Un message de confirmation doit être affiché après la déconnexion.

## Données
- **Entrée** : Clic sur le bouton de déconnexion.
- **Sortie** : Redirection vers `/login` avec un message de confirmation.

## Liens
- [Spécifications techniques de la topbar](../../_app/templates/partials/topbar.spec.md)
- [Spécifications des routes d'authentification](../../_app/blueprints/auth/auth.routes.spec.md)