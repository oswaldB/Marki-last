# Suivi des Spécifications Techniques (ST)

**Date** : 2026-01-18
**Auteur** : Mistral Vibe
**Statut** : En cours

---

## **Tableau de Suivi**

| ST | Titre | Statut | Spécifications | Tests | Implémentation | Erreurs Console |
|----|-------|--------|---------------|-------|----------------|-----------------|
| ST-001 | Hello World | ✅ Validé | ✅ | ✅ | ✅ | ❌ |
| ST-002 | Base Layout avec Tailwind et Alpine.js | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-003 | Layout Dashboard avec Sidebar et Topbar | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-004 | Layout Simple sans Authentification | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-005 | Layout Simple avec Authentification | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-006 | Page de Connexion | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-007 | Mot de Passe Oublié | ❌ Non commencé | ❌ | ❌ | ❌ | ❌ |
| ST-008 | Page SuperAdmin | ✅ Validé | ✅ | ✅ | ✅ | ❌ |
| ST-009 | Synchroniser les impayés depuis Marki Mirroir | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-010 | Créer une liste manuelle | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-011 | Modifier une liste manuelle | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-012 | Créer une liste automatique | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-013 | Supprimer une liste | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-014 | Créer une séquence d’emails | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-015 | Associer une liste à une séquence | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-016 | Activer une séquence | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-017 | Désactiver une séquence | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-018 | Modifier une séquence | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-019 | Envoyer les emails quotidiens | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-020 | Gérer les échecs d’envoi | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-021 | Visualiser le calendrier des relances | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-022 | Modifier un email via un drawer | ✅ Validé | ✅ | ❌ | ❌ | ❌ |
| ST-023 | Consulter la page des emails manquants | ✅ Validé | ✅ | ❌ | ❌ | ❌ |

---

## **Légende**

- ✅ Validé : La spécification est complète et tous les tests passent.
- ❌ En cours : La spécification est en cours de développement.
- ❌ Non commencé : La spécification n'a pas encore été démarrée.

---

## **Détails des Spécifications**

### ST-001 : Hello World
- **Spécifications** : [ST-001_hello-world-functionnelles.md](specs/specs/ST-001_hello-world-functionnelles.md)
- **Spécifications Techniques** : [hello_world.spec](specs/_app/blueprints/hello/hello_world.spec)
- **Tests** : [ST-001_hello_world.spec.ts](tests/ST-001_hello_world.spec.ts)
- **Implémentation** : [hello/routes.py](app/blueprints/hello/routes.py)
- **Rapport** : [ST-001-rapport.md](reports/ST-001-rapport.md)

### ST-002 : Base Layout avec Tailwind et Alpine.js
- **Spécifications** : [ST-002_base-layout-functionnelles.md](specs/specs/ST-002_base-layout-functionnelles.md)
- **Spécifications Techniques** : [base.html.spec](specs/_app/templates/base.html.spec)
- **Tests** : [ST-002_base_layout.spec.ts](tests/ST-002_base_layout.spec.ts)
- **Implémentation** : [base.html](app/templates/base.html)

### ST-003 : Layout Dashboard avec Sidebar et Topbar
- **Spécifications** : [ST-003_dashboard-layout-functionnelles.md](specs/specs/ST-003_dashboard-layout-functionnelles.md)
- **Spécifications Techniques** : [dashboard.html.spec](specs/_app/templates/dashboard.html.spec)
- **Tests** : [ST-003_dashboard_layout.spec.ts](tests/ST-003_dashboard_layout.spec.ts)
- **Implémentation** : [dashboard.html](app/templates/dashboard.html)

### ST-004 : Layout Simple sans Authentification
- **Spécifications** : [ST-004_simple-layout-functionnelles.md](specs/specs/ST-004_simple-layout-functionnelles.md)
- **Spécifications Techniques** : [simple.html.spec](specs/_app/templates/simple.html.spec)
- **Tests** : [ST-004_simple_layout.spec.ts](tests/ST-004_simple_layout.spec.ts)
- **Implémentation** : [simple.html](app/templates/simple.html)

### ST-005 : Layout Simple avec Authentification
- **Spécifications** : [ST-005_simple-auth-layout-functionnelles.md](specs/specs/ST-005_simple-auth-layout-functionnelles.md)
- **Spécifications Techniques** : [simple_auth.html.spec](specs/_app/templates/simple_auth.html.spec)
- **Tests** : [ST-005_simple_auth_layout.spec.ts](tests/ST-005_simple_auth_layout.spec.ts)
- **Implémentation** : [simple_auth.html](app/templates/simple_auth.html)

### ST-006 : Page de Connexion
- **Spécifications** : [ST-006_login-page-functionnelles.md](specs/specs/ST-006_login-page-functionnelles.md)
- **Spécifications Techniques** : [login.py.spec](specs/_app/blueprints/auth/login.py.spec)
- **Tests** : [ST-006_login_page.spec.ts](tests/ST-006_login_page.spec.ts)
- **Implémentation** : [auth/routes.py](app/blueprints/auth/routes.py)

### ST-007 : Mot de Passe Oublié
- **Spécifications** : ❌ Non commencé
- **Spécifications Techniques** : ❌ Non commencé
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-008 : Page SuperAdmin
- **Spécifications** : [ST-008_superadmin-page-functionnelles.md](specs/specs/ST-008_superadmin-page-functionnelles.md)
- **Spécifications Techniques** : [users.py.spec](specs/_app/blueprints/users/users.py.spec)
- **Tests** : [ST-008_superadmin_page.spec.ts](tests/ST-008_superadmin_page.spec.ts)
- **Implémentation** : [users/routes.py](app/blueprints/users/routes.py)
- **Rapport** : [ST-008-rapport.md](reports/ST-008-rapport.md)

### ST-009 : Synchroniser les impayés depuis Marki Mirroir
- **Spécifications** : [ST-009_synchronisation-impayes-functionnelles.md](specs/specs/ST-009_synchronisation-impayes-functionnelles.md)
- **Spécifications Techniques** : [synchronisation.spec](specs/_app/blueprints/impayes/synchronisation.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-010 : Créer une liste manuelle
- **Spécifications** : [ST-010_creer-liste-manuelle-functionnelles.md](specs/specs/ST-010_creer-liste-manuelle-functionnelles.md)
- **Spécifications Techniques** : [liste_manuelle.spec](specs/_app/blueprints/impayes/liste_manuelle.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-011 : Modifier une liste manuelle
- **Spécifications** : [ST-011_modifier-liste-manuelle-functionnelles.md](specs/specs/ST-011_modifier-liste-manuelle-functionnelles.md)
- **Spécifications Techniques** : [liste_manuelle.spec](specs/_app/blueprints/impayes/liste_manuelle.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-012 : Créer une liste automatique
- **Spécifications** : [ST-012_creer-liste-automatique-functionnelles.md](specs/specs/ST-012_creer-liste-automatique-functionnelles.md)
- **Spécifications Techniques** : [liste_automatique.spec](specs/_app/blueprints/impayes/liste_automatique.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-013 : Supprimer une liste
- **Spécifications** : [ST-013_supprimer-liste-functionnelles.md](specs/specs/ST-013_supprimer-liste-functionnelles.md)
- **Spécifications Techniques** : [liste_manuelle.spec](specs/_app/blueprints/impayes/liste_manuelle.spec) et [liste_automatique.spec](specs/_app/blueprints/impayes/liste_automatique.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-014 : Créer une séquence d’emails
- **Spécifications** : [ST-014_creer-sequence-emails-functionnelles.md](specs/specs/ST-014_creer-sequence-emails-functionnelles.md)
- **Spécifications Techniques** : [sequence_emails.spec](specs/_app/blueprints/sequences/sequence_emails.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-015 : Associer une liste à une séquence
- **Spécifications** : [ST-015_associer-liste-sequence-functionnelles.md](specs/specs/ST-015_associer-liste-sequence-functionnelles.md)
- **Spécifications Techniques** : [sequence_emails.spec](specs/_app/blueprints/sequences/sequence_emails.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-016 : Activer une séquence
- **Spécifications** : [ST-016_activer-sequence-functionnelles.md](specs/specs/ST-016_activer-sequence-functionnelles.md)
- **Spécifications Techniques** : [sequence_emails.spec](specs/_app/blueprints/sequences/sequence_emails.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-017 : Désactiver une séquence
- **Spécifications** : [ST-017_desactiver-sequence-functionnelles.md](specs/specs/ST-017_desactiver-sequence-functionnelles.md)
- **Spécifications Techniques** : [sequence_emails.spec](specs/_app/blueprints/sequences/sequence_emails.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-018 : Modifier une séquence
- **Spécifications** : [ST-018_modifier-sequence-functionnelles.md](specs/specs/ST-018_modifier-sequence-functionnelles.md)
- **Spécifications Techniques** : [sequence_emails.spec](specs/_app/blueprints/sequences/sequence_emails.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-019 : Envoyer les emails quotidiens
- **Spécifications** : [ST-019_envoyer-emails-quotidiens-functionnelles.md](specs/specs/ST-019_envoyer-emails-quotidiens-functionnelles.md)
- **Spécifications Techniques** : [relances_actions.spec](specs/_app/blueprints/sequences/relances_actions.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-020 : Gérer les échecs d’envoi
- **Spécifications** : [ST-020_gerer-echecs-envoi-functionnelles.md](specs/specs/ST-020_gerer-echecs-envoi-functionnelles.md)
- **Spécifications Techniques** : [relances_actions.spec](specs/_app/blueprints/sequences/relances_actions.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-021 : Visualiser le calendrier des relances
- **Spécifications** : [ST-021_visualiser-calendrier-relances-functionnelles.md](specs/specs/ST-021_visualiser-calendrier-relances-functionnelles.md)
- **Spécifications Techniques** : [relances_actions.spec](specs/_app/blueprints/sequences/relances_actions.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-022 : Modifier un email via un drawer
- **Spécifications** : [ST-022_modifier-email-drawer-functionnelles.md](specs/specs/ST-022_modifier-email-drawer-functionnelles.md)
- **Spécifications Techniques** : [relances_actions.spec](specs/_app/blueprints/sequences/relances_actions.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

### ST-023 : Consulter la page des emails manquants
- **Spécifications** : [ST-023_consulter-emails-manquants-functionnelles.md](specs/specs/ST-023_consulter-emails-manquants-functionnelles.md)
- **Spécifications Techniques** : [synchronisation.spec](specs/_app/blueprints/impayes/synchronisation.spec)
- **Tests** : ❌ Non commencé
- **Implémentation** : ❌ Non commencé

---

## **Résumé des Progrès**

- **Total des ST** : 23
- **ST Validées** : 2 (ST-001, ST-008)
- **ST En Cours** : 15 (ST-002, ST-003, ST-004, ST-005, ST-006, ST-009 à ST-023)
- **ST Non Commencées** : 1 (ST-007)

---

## **Prochaines Étapes**

1. **ST-002 à ST-006** : Finaliser les tests et l'implémentation.
2. **ST-007** : Commencer les spécifications et l'implémentation.
3. **ST-009 à ST-023** : Créer les tests et implémenter les fonctionnalités.
4. **Vérification des Erreurs Console** : Analyser et corriger les erreurs console pour toutes les ST.

---

**Dernière Mise à Jour** : 2026-01-18