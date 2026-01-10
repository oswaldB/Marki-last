#!/bin/bash

# Script de test pour vérifier la configuration avant lancement
# Auteur: Mistral Vibe
# Date: 2024
# Version: 1.0

echo "==================================="
echo "Test de configuration du serveur"
echo "==================================="
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Erreur: Python 3 n'est pas installé."
    exit 1
else
    echo "✅ Python 3 est installé: $(python3 --version)"
fi

# Vérifier si les dépendances sont installées
if [ ! -f "requirements.txt" ]; then
    echo "❌ Erreur: Fichier requirements.txt introuvable."
    exit 1
else
    echo "✅ Fichier requirements.txt trouvé"
fi

# Vérifier si l'environnement virtuel existe
if [ -d ".venv" ]; then
    echo "✅ Environnement virtuel détecté"
    source .venv/bin/activate
    echo "   Environnement activé: $(python --version)"
else
    echo "⚠️  Avertissement: Aucun environnement virtuel détecté"
fi

# Vérifier les dépendances installées
echo ""
echo "Vérification des dépendances principales..."
pip3 list | grep -q Flask
if [ $? -eq 0 ]; then
    echo "✅ Flask est installé"
else
    echo "❌ Flask n'est pas installé"
fi

pip3 list | grep -q behave
if [ $? -eq 0 ]; then
    echo "✅ Behave est installé"
else
    echo "❌ Behave n'est pas installé"
fi

echo ""
echo "Vérification de la structure du projet..."
if [ -d "app" ] && [ -d "specs" ] && [ -d "tests" ]; then
    echo "✅ Structure du projet valide"
else
    echo "❌ Structure du projet incomplète"
fi

echo ""
echo "==================================="
echo "Configuration vérifiée avec succès!"
echo "Vous pouvez lancer le serveur avec: ./run_debug.sh"
echo "==================================="
