# ST-005 : Relance des Factures Impayées
**Date** : 2026-01-13
**Auteur** : Oswald Bernard
**Statut** : ST-005.md (validé)

---
## **1. Contexte et Objectifs**
- **Problème résolu** : Permettre aux utilisateurs de gérer les relances des factures impayées, y compris la création de campagnes de relance, la sélection des factures, et l'envoi des notifications.
- **Acteurs impliqués** : Développeurs backend, frontend, designers, testeurs.
- **Valeur ajoutée** : Une application web sécurisée et intuitive pour la gestion des relances des factures impayées.

---
## **2. Flux Principal**
1. L'utilisateur accède à la page `/relances/dashboard`.
2. Flask renvoie un résumé des campagnes actives et pausées, ainsi que des statistiques sur les relances.
3. Les campagnes sont affichées dans la page.
4. L'utilisateur accède à la page `/relances/calendrier`.
5. Flask renvoie un calendrier des emails/SMS envoyés et à envoyer.
6. Le calendrier est affiché dans la page.
7. L'utilisateur peut marquer manuellement une relance comme envoyée ou échouée.
8. L'utilisateur peut visualiser les détails d'un envoi.
9. L'utilisateur peut modifier les messages des relances via un drawer.
10. L'utilisateur accède à la page `/relances/campagnes`.
11. L'utilisateur peut créer ou éditer une campagne de relance.
12. L'utilisateur peut mettre en pause ou reprendre une campagne.
13. L'utilisateur peut supprimer une campagne.
14. L'utilisateur peut lister toutes les campagnes.
15. L'utilisateur peut définir une séquence d'emails/SMS pour une campagne.
16. L'utilisateur peut prévisualiser une séquence avant activation.
17. Le système génère les emails/SMS à envoyer pour une campagne active.
18. L'utilisateur peut utiliser des variables dynamiques dans les messages des séquences.
19. L'utilisateur peut générer un template d'email avec ChatGPT en utilisant les variables dynamiques.
20. L'utilisateur peut afficher le prompt utilisé pour générer le template d'email avec ChatGPT.
21. L'utilisateur accède à la page `/relances/criteres`.
22. L'utilisateur peut définir des critères automatiques pour sélectionner les factures à relancer.
23. Le système planifie le peuplement automatique des listes de factures.
24. L'utilisateur peut afficher les factures sans email valide.
25. L'utilisateur peut sélectionner manuellement des factures pour une campagne.
26. L'utilisateur peut rafraîchir manuellement la liste des factures impayées.
27. Le système récupère les factures impayées via une requête SQL.
28. Le système synchronise les statuts des factures avant chaque envoi de relance.
29. Le système envoie les relances.
30. Le système notifie l'utilisateur en cas d'email manquant ou d'échec d'envoi.

---
## **3. Règles Métier**
- **Contraintes** :
  - Une relance ne doit pas être envoyée si la facture est déjà payée.
  - Les relances doivent être envoyées selon les délais définis dans la séquence.
  - Les emails/SMS doivent contenir des variables dynamiques (nom du client, montant dû, etc.).
  - Une campagne ne peut être supprimée que si elle est en pause.
  - Une campagne ne peut être activée que si elle inclut des critères de sélection et une séquence d'emails.
  - Les critères automatiques sont appliqués tous les jours à 17h pour sélectionner les factures.
  - Les critères manuels peuvent être rafraîchis manuellement.
  - Les factures impayées sont récupérées via une requête SQL sur une base de données externe.
  - Les statuts des factures sont synchronisés avant chaque envoi de relance.
- **Validations** :
  - Les critères de sélection des factures doivent être cohérents et complets.
  - Les séquences d'emails/SMS doivent être définies et validées avant activation.
  - Les variables dynamiques doivent être remplacées par les valeurs correspondantes.
- **Sécurité** :
  - Les données des factures et des campagnes doivent être sécurisées et protégées.
  - Les routes doivent être protégées contre les accès non autorisés.

---
## **4. Maquettes et Exemples**
```
+-----------------------------------------------------+
| Topbar                                             |
| +-------------+-------------------------------------+ |
| | Sidebar     | Dashboard des Relances            | |
| |             |                                     | |
| |             | +---------------------------------+ | |
| |             | | Résumé des Campagnes             | | |
| |             | +---------------------------------+ | |
| |             |                                     | |
| |             | +---------------------------------+ | |
| |             | | Calendrier des Envois            | | |
| |             | +---------------------------------+ | |
| +-------------+-------------------------------------+ |
+-----------------------------------------------------+
```

---
## **5. Liens Vers les Spécifications Techniques**
- [Routes](/_app/blueprints/relance.routes.spec.md)
- [Modèles](/_app/blueprints/relance.models.spec.md)
- [Composants](/_app/blueprints/relance/templates/partials/)
- [Scripts](/_app/blueprints/relance/scripts/)