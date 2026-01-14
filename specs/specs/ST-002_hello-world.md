# Spécification : Page Hello World avec Logo

**ID** : ST-005
**Date** : 2024-10-05
**Acteur** : Specificator

---

## Description
La page "Hello World" est une page simple qui affiche un message de bienvenue et le logo de Marki. Cette page sert de point d'entrée pour les utilisateurs et doit être accessible sans authentification.

## Fonctionnalités
1. Afficher un message de bienvenue : "Hello, World!"
2. Afficher le logo de Marki (fichier : `public/logo.png`).
3. Le logo doit être centré au-dessus du message.
4. La page doit être responsive et s'adapter à tous les types d'écrans.

## Maquettes
- Le logo doit avoir une largeur maximale de 200px.
- Le message doit être en dessous du logo, avec une marge de 20px.
- Le texte doit être centré et avoir une taille de 24px.

## Règles Métier
- Aucune authentification requise pour accéder à cette page.
- La page doit être accessible via l'URL `/hello`.

## Intégration
- **Backend** : Aucune logique backend requise.
- **Frontend** : Utiliser HTML/CSS pur ou un template Flask simple.
- **Logo** : Le logo doit être placé dans le dossier `public/logo.png`.

## Exemple de Code (Template)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World - Marki</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .logo {
            max-width: 200px;
            margin-bottom: 20px;
        }
        .message {
            font-size: 24px;
        }
    </style>
</head>
<body>
    <img src="/public/logo.png" alt="Logo Marki" class="logo">
    <div class="message">Hello, World!</div>
</body>
</html>
```

## Liens
- [Styleguide](styleguide.md)
- [Tests associés](tests/features/hello_world.feature)
