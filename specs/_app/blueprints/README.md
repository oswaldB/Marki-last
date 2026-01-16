# Blueprints - Spécifications

Ce dossier contient les spécifications pour les blueprints de l'application Flask. Les blueprints sont organisés en sous-dossiers pour refléter la structure de l'application.

## Organisation

- **auth/** : Spécifications pour les blueprints liés à l'authentification, y compris la connexion, la déconnexion, et la récupération de mot de passe.
- **users/** : Spécifications pour les blueprints liés à la gestion des utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs.

## Structure des Fichiers

Chaque fichier de spécifications suit une structure standard pour décrire les fonctionnalités, les routes, les paramètres, et les retours des blueprints. Voici un exemple de la structure d'un fichier de spécifications :

```markdown
# Blueprint: <nom_du_blueprint>.py
**Fichier miroir** : `app/blueprints/<nom_du_blueprint>.py`
**Description** : Description du blueprint et de ses fonctionnalités.

---

## 🔧 Fonctions

### `<nom_de_la_fonction>`
**Description** :
- Description de la fonction et de ses responsabilités.

**Route** :
- **<MÉTHODE> <ROUTE>** : Description de la route et de son utilisation.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| param1    | str    | Description du paramètre 1           | "exemple1"      |
| param2    | int    | Description du paramètre 2           | 123              |

**Retour** :
- Description des retours possibles de la fonction.

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| var1      | str    | Description de la variable globale 1 | "exemple1"      |
| var2      | int    | Description de la variable globale 2 | 123              |

## 📋 Flux Principal
1. Étape 1 du flux principal.
2. Étape 2 du flux principal.
3. Étape 3 du flux principal.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT <NOM>         |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - <fonction1>                |  |
|  |  - <fonction2>                |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - <variable1>                |  |
|  |  - <variable2>                |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Étape 1                   |  |
|  |  2. Étape 2                   |  |
|  |  3. Étape 3                   |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

## Exemples

- **auth/login.py.spec** : Spécifications pour la connexion et la déconnexion des utilisateurs.
- **users/users.py.spec** : Spécifications pour la gestion des utilisateurs, y compris la création, l'activation, et la modification des mots de passe.

## Bonnes Pratiques

1. **Nommage des Fichiers** : Utilisez des noms de fichiers qui reflètent clairement le blueprint et la fonctionnalité. Par exemple, `auth_login.py.spec` pour les spécifications de connexion.

2. **Documentation** : Assurez-vous que chaque fichier de spécifications contient des commentaires et des en-têtes clairs pour expliquer le but du blueprint et les fonctionnalités qu'il couvre.

3. **Organisation** : Regroupez les spécifications par blueprint et utilisez des sous-dossiers pour maintenir une structure claire et intuitive.

4. **Mise à Jour** : Mettez à jour les références aux fichiers de spécifications dans la documentation et les autres fichiers pour refléter la structure actuelle.

En suivant ces bonnes pratiques, vous pouvez maintenir une structure claire et facile à comprendre pour les spécifications des blueprints.