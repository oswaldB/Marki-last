#!/bin/bash

# Script de lancement du serveur Flask en mode debug
# Auteur: Mistral Vibe
# Date: 2024
# Version: 1.0

echo "==================================="
echo "Lancement du serveur Flask (DEBUG)"
echo "==================================="
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "Erreur: Python 3 n'est pas installé."
    exit 1
fi

# Vérifier si les dépendances sont installées
if [ ! -f "requirements.txt" ]; then
    echo "Erreur: Fichier requirements.txt introuvable."
    exit 1
fi

# Vérifier si l'environnement virtuel existe
echo "Vérification de l'environnement virtuel..."
if [ -d ".venv" ]; then
    echo "Activation de l'environnement virtuel..."
    source .venv/bin/activate
else
    echo "Avertissement: Aucun environnement virtuel détecté. Utilisation de Python système."
fi

# Vérifier les dépendances installées
echo "Vérification des dépendances..."
pip3 list | grep -q Flask
if [ $? -ne 0 ]; then
    echo "Installation des dépendances..."
    pip3 install -r requirements.txt
fi

echo ""
echo "Démarrage du serveur Flask en mode DEBUG..."
echo "URL: http://localhost:5000"
echo "Appuyez sur Ctrl+C pour arrêter le serveur."
echo ""
echo "==================================="
echo ""

# Lancer le serveur Flask
python3 app.py

echo ""
echo "Serveur arrêté."
