# Hello World - ST-002

## Description
Création d'une page simple "Hello World" pour démontrer le fonctionnement de base de l'application.

## Spécifications Techniques

### Route
- **URL** : `/hello`
- **Méthode** : GET
- **Titre** : "Hello World - Marki"

### Contenu
La page doit afficher :
- Un titre principal "Hello World"
- Un sous-titre "Bienvenue sur Marki"
- Un paragraphe de texte explicatif
- Un bouton de retour à l'accueil

### Structure HTML
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - Marki</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-md max-w-md w-full text-center">
        <h1 class="text-3xl font-bold text-gray-800 mb-4">Hello World</h1>
        <h2 class="text-xl text-gray-600 mb-6">Bienvenue sur Marki</h2>
        <p class="text-gray-700 mb-8">
            Ceci est une page de démonstration pour vérifier le bon fonctionnement 
            de l'application Marki.
        </p>
        <a href="/" class="inline-block bg-blue-500 hover:bg-blue-600 text-white 
                          font-medium py-2 px-4 rounded transition duration-200">
            Retour à l'accueil
        </a>
    </div>
</body>
</html>
```

### Comportement
- La page doit être accessible sans authentification
- Le bouton doit rediriger vers la page d'accueil (`/`)
- La page doit être responsive et s'afficher correctement sur mobile

### Tests
- Vérifier que la page affiche le titre "Hello World"
- Vérifier que la page affiche le sous-titre "Bienvenue sur Marki"
- Vérifier que le bouton de retour à l'accueil est présent et fonctionnel
- Vérifier que la page est accessible sans authentification

## Critères d'acceptation
- [ ] La page est accessible à l'URL `/hello`
- [ ] Le titre principal "Hello World" est affiché
- [ ] Le sous-titre "Bienvenue sur Marki" est affiché
- [ ] Le paragraphe explicatif est présent
- [ ] Le bouton de retour à l'accueil est présent et fonctionnel
- [ ] La page est responsive
- [ ] Tous les tests passent