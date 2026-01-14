# language: fr
Fonctionnalité: Page Hello World avec Logo
  En tant qu'utilisateur,
  Je veux voir une page de bienvenue avec le logo de Marki
  Afin de confirmer que l'application est opérationnelle.

  Contexte:
    Étant donné que je suis sur la page d'accueil

  Scénario: Affichage du logo et du message
    Quand je visite la page "/hello"
    Alors je devrais voir un élément "img" avec l'attribut "src" égal à "/public/logo.png"
    Et je devrais voir un texte "Hello, World!"
    Et le logo devrait avoir une classe "logo"
    Et le message devrait avoir une classe "message"

  Scénario: Style du logo
    Quand je visite la page "/hello"
    Alors l'élément "img.logo" devrait avoir un style "max-width" égal à "200px"
    Et l'élément "img.logo" devrait avoir un style "margin-bottom" égal à "20px"

  Scénario: Style du message
    Quand je visite la page "/hello"
    Alors l'élément ".message" devrait avoir un style "font-size" égal à "24px"
    Et l'élément "body" devrait avoir un style "text-align" égal à "center"
