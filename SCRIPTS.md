# Scripts de Lancement du Serveur Flask

Ce document décrit les différents scripts disponibles pour lancer le serveur Flask en mode debug.

## Table des Matières
- [Script Bash (run_debug.sh)](#script-bash-run_debugsh)
- [Script Python (run_server.py)](#script-python-run_serverpy)
- [Variables d'Environnement](#variables-denvironnement)
- [Dépannage](#dépannage)

## Script Bash (run_debug.sh)

Script principal pour lancer le serveur Flask avec vérifications préalables.

### Utilisation
```bash
./run_debug.sh
```

### Fonctionnalités
- Vérifie la présence de Python 3
- Vérifie le fichier requirements.txt
- Active l'environnement virtuel si présent
- Vérifie les dépendances Flask
- Lance le serveur avec app.py

### Sortie
```
===================================
Lancement du serveur Flask (DEBUG)
===================================

Démarrage du serveur Flask en mode DEBUG...
URL: http://localhost:5000
Appuyez sur Ctrl+C pour arrêter le serveur.

===================================
```

## Script Python (run_server.py)

Script Python alternatif avec plus d'options de configuration.

### Utilisation
```bash
python3 run_server.py
```

### Options via Variables d'Environnement
- `FLASK_HOST`: Hôte (par défaut: 0.0.0.0)
- `FLASK_PORT`: Port (par défaut: 5000)
- `FLASK_DEBUG`: Mode debug (par défaut: true)

### Exemple avec variables personnalisées
```bash
export FLASK_HOST=127.0.0.1
export FLASK_PORT=8080
export FLASK_DEBUG=false
python3 run_server.py
```

### Sortie
```
====================================================
Lancement du serveur Flask (Mode DEBUG)
====================================================

Configuration:
  Hôte: 0.0.0.0
  Port: 5000
  Mode Debug: ACTIF

URL: http://0.0.0.0:5000
Appuyez sur Ctrl+C pour arrêter le serveur.
====================================================
```

## Variables d'Environnement

| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| FLASK_HOST | Adresse IP du serveur | 0.0.0.0 |
| FLASK_PORT | Port du serveur | 5000 |
| FLASK_DEBUG | Mode debug | true |

## Dépannage

### Problème: Port déjà utilisé
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Trouver le processus utilisant le port
lsof -i :5000

# Tuer le processus (remplacer PID par l'ID réel)
kill -9 PID
```

### Problème: Dépendances manquantes
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Installer les dépendances
pip3 install -r requirements.txt
```

### Problème: Permission refusée
```
bash: ./run_debug.sh: Permission non accordée
```

**Solution:**
```bash
chmod +x run_debug.sh
```

## Notes

- Le mode debug active le rechargement automatique du code
- Les erreurs sont affichées dans le navigateur avec des détails
- Le serveur est accessible depuis le réseau local avec `0.0.0.0`
- Pour un usage en production, désactivez le mode debug
