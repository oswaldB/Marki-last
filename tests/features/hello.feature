# language: fr
Fonctionnalité: Page de salutation personnalisée
  En tant qu'utilisateur,
  Je veux une page qui me salue avec mon prénom,
  Afin de me sentir accueilli.

  Contexte:
    Étant donné que je suis sur la page "/hello"

  Scénario: Salutation sans prénom
    Quand je visite la page "/hello"
    Alors je dois voir le message "Bonjour !"

  Scénario: Salutation avec prénom
    Quand je visite la page "/hello/toto"
    Alors je dois voir le message "Bonjour toto !"
