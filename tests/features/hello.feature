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

  Scénario: Changer de prénom
    Quand je visite la page "/hello/toto"
    Et je clique sur "Pas le bon prénom ?"
    Alors je dois voir un formulaire pour changer le prénom
    Quand je saisis "titi" dans le formulaire
    Et je clique sur "Changer"
    Alors je dois voir le message "Bonjour titi !"
