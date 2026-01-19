# Blueprint: Gestion des relances et actions
**Fichier miroir** : `app/blueprints/sequences/relances_actions.py`
**Description** : Blueprint pour gérer les relances et les actions d'envoi d'emails.

---

## 🔧 Fonctions

### `envoyer_emails_quotidiens()`
**Description** :
- Envoie les emails quotidiens à 18h.
- Vérifie les impayés dans `relances-actions` et envoie les emails si le statut est "impayé".

**Route** :
- **POST /envoyer-emails** : Lance l'envoi des emails quotidiens.

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `gerer_echecs_envoi()`
**Description** :
- Gère les échecs d'envoi d'emails.
- Envoie un email d'alerte à `email_notification` (défini dans `.env`).

**Route** :
- **POST /gerer-echecs** : Gère les échecs d'envoi.

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `visualiser_calendrier_relances()`
**Description** :
- Visualise les emails (envoyés/à envoyer) dans un calendrier interactif.
- Permet l'application de filtres.

**Route** :
- **GET /calendrier-relances** : Affiche le calendrier des relances.

**Retour** :
- Rend le template `calendrier_relances.html` avec les données des relances.

### `modifier_email_drawer(email_id)`
**Description** :
- Modifie un email via un drawer.
- Recalcule les variables du template si nécessaire.

**Route** :
- **PUT /emails/<email_id>/modifier** : Modifie un email.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| email_id | int | ID de l'email à modifier | 1 |
| contenu | str | Nouveau contenu de l'email | "Bonjour {{nom}}" |
| date_envoi | str | Nouvelle date d'envoi | "2026-01-18" |
| destinataire | str | Nouveau destinataire | "email@example.com" |

**Retour** :
- Message de succès ou d'erreur au format JSON.

---

## 📝 Variables Globales

| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| `db` | SQLite | Instance de la base de données SQLite | `sqlite3.connect('marki.db')` |
| `EMAIL_NOTIFICATION` | str | Email de notification pour les échecs | "admin@example.com" |

---

## 📋 Flux Principal

1. **Envoi des emails quotidiens** :
   - À 18h, vérifier les impayés dans `relances-actions`.
   - Envoyer les emails si le statut est "impayé".
   - Mettre à jour le statut après l'envoi.

2. **Gestion des échecs d'envoi** :
   - En cas d'échec, envoyer un email d'alerte à `email_notification`.
   - Ne pas effectuer de réessai automatique.

3. **Visualisation du calendrier des relances** :
   - Accéder au calendrier des relances.
   - Appliquer des filtres pour afficher les emails envoyés ou à envoyer.

4. **Modification d'un email via un drawer** :
   - Sélectionner un email à modifier.
   - Ouvrir le drawer de modification.
   - Modifier le contenu, la date ou le destinataire.
   - Enregistrer les modifications.

---

## 📊 Structure de la Base de Données SQLite

### Table `relances_actions`

```sql
CREATE TABLE relances_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    template TEXT NOT NULL,
    date_envoi TEXT NOT NULL,
    statut TEXT NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequences(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications

- **id** : Identifiant unique de l'action, auto-incrémenté.
- **sequence_id** : ID de la séquence.
- **impaye_id** : ID de l'impayé.
- **template** : Template de l'email.
- **date_envoi** : Date d'envoi de l'email.
- **statut** : Statut de l'action (par exemple, "à envoyer", "envoyé", "erreur").

---

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT RELANCES ACTIONS |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - envoyer_emails_quotidiens()|  |
|  |  - gerer_echecs_envoi()       |  |
|  |  - visualiser_calendrier()    |  |
|  |  - modifier_email_drawer()    |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (SQLite)                |  |
|  |  - EMAIL_NOTIFICATION         |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Envoyer emails quotidiens |  |
|  |  2. Gérer échecs d'envoi      |  |
|  |  3. Visualiser calendrier     |  |
|  |  4. Modifier email           |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
