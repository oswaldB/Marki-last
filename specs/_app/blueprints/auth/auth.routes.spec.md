# Routes : Authentification (ST-003, ST-008)
**Fichier cible** : `app/blueprints/auth/routes.py`

---

## **Endpoints**

| URL | Méthode | Paramètres | Retour | Description |
|-----|---------|-----------|--------|-------------|
| `/auth/login` | GET | - | HTML | Formulaire de connexion |
| `/auth/login` | POST | `username`, `password` | Redirect | Traite la connexion |
| `/auth/register` | GET | - | HTML | Formulaire d'inscription |
| `/auth/register` | POST | `username`, `password`, `password_confirm` | Redirect | Crée un compte |
| `/auth/logout` | POST | - | Redirect | Déconnecte l'utilisateur |
| `/auth/forgot-password` | GET | - | HTML | Formulaire de récupération |
| `/auth/forgot-password` | POST | `username` | Redirect | Génère mot de passe temporaire |
| `/superadmin` | GET | - | HTML | Affiche le formulaire de création du premier administrateur |
| `/superadmin` | POST | `superadmin_password`, `username`, `password`, `confirm_password` | Redirect | Crée le premier administrateur et redirige vers `/auth/login` |
| `/settings/team` | GET | - | HTML | Gestion des utilisateurs (admin) |
| `/api/users` | GET | - | JSON | Liste des utilisateurs |
| `/api/users/add` | POST | `username`, `password`, `email` | JSON | Ajoute collaborateur |
| `/api/users/<id>/password` | PUT | `new_password` | JSON | Change mot de passe |
| `/api/users/<id>/toggle` | PUT | - | JSON | Bascule état bloqué/actif |

---

## **Règles Métier**

### Authentification
- `username` doit être **unique** et alphanumérioque (3-50 caractères)
- `password` doit être **haché** avec bcrypt
- `password` minimum **8 caractères** avec majuscule, minuscule, chiffre
- Les tentatives de connexion échouées sont limitées à 5 avant blocage temporaire

### Inscription
- L'utilisateur doit confirmer le mot de passe
- L'email est optionnel mais unique s'il est fourni
- Après inscription, redirection vers `/auth/login`

### Récupération Mot de Passe
- Générer un mot de passe temporaire aléatoire (12 caractères)
- Afficher le mot de passe à l'écran UNE SEULE FOIS
- Forcer changement au prochain login

### Superadmin
- Accessible uniquement avec le mot de passe `Citron6-Mustang9`
- Vérifie qu'aucun administrateur n'existe déjà avant de créer un nouvel utilisateur
- L'utilisateur créé doit avoir le rôle `admin` et le statut `actif`
- Après création, redirige vers `/auth/login`

### Gestion Équipe (Admin)
- Accessible **uniquement** si `isAdmin = true`
- Administrateur peut : créer utilisateur, changer mot de passe, bloquer/débloquer
- Email du nouvel utilisateur est unique

---

## **Codes d'Erreur**

| Code | Message | Contexte |
|------|---------|----------|
| `400` | Données invalides | Format incorrect ou champs manquants |
| `401` | Identifiants invalides | Username/password incorrect |
| `403` | Accès refusé | Utilisateur bloqué ou non admin |
| `409` | Username/Email existe | Conflit d'unicité |
| `500` | Erreur serveur | Exception non gérée |
