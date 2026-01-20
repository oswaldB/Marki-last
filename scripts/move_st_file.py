#!/usr/bin/env python3

import os
import sys
import shutil
from datetime import datetime

# Chemins des dossiers
dirs = {
    "01_specs_fonctionnelles": "specs/process/01_specs_fonctionnelles",
    "02_specs_techniques": "specs/process/02_specs_techniques",
    "03_redaction_tests": "specs/process/03_redaction_tests",
    "04_developpement_bdd": "specs/process/04_developpement_bdd",
    "05_developpement_back": "specs/process/05_developpement_back",
    "06_developpement_front": "specs/process/06_developpement_front",
    "07_execution_tests": "specs/process/07_execution_tests",
    "08_tests_reussis": "specs/process/08_tests_reussis",
    "09_tests_echoues": "specs/process/09_tests_echoues"
}

def move_st_file(source_dir, target_dir, st_number):
    """
    Déplace un fichier ST- d'un dossier source à un dossier cible.
    
    Args:
        source_dir (str): Dossier source.
        target_dir (str): Dossier cible.
        st_number (str): Numéro du fichier ST-.
    """
    # Vérifier que les dossiers source et cible existent
    if source_dir not in dirs:
        print(f"Erreur: Le dossier source {source_dir} n'existe pas.")
        return
    
    if target_dir not in dirs:
        print(f"Erreur: Le dossier cible {target_dir} n'existe pas.")
        return
    
    # Trouver le fichier ST- dans le dossier source
    source_path = dirs[source_dir]
    files = [f for f in os.listdir(source_path) if f.startswith(f"ST-{st_number}")]
    
    if not files:
        print(f"Erreur: Aucun fichier ST-{st_number} trouvé dans {source_dir}.")
        return
    
    # Déplacer le fichier vers le dossier cible
    target_path = dirs[target_dir]
    for file in files:
        shutil.move(os.path.join(source_path, file), os.path.join(target_path, file))
        print(f"Fichier {file} déplacé de {source_dir} vers {target_dir}.")
    
    # Ajouter l'aval du Global Manager au fichier
    file_path = os.path.join(target_path, files[0])
    with open(file_path, 'a') as f:
        f.write(f"\n---\n\n## 📌 Aval du Global Manager\n\n**Date** : {datetime.now().strftime('%Y-%m-%d')}\n**Statut** : Validé\n**Commentaires** : Le travail a été validé et le fichier a été déplacé vers le dossier suivant.\n")

def main():
    if len(sys.argv) != 4:
        print("Usage: python move_st_file.py <source_dir> <target_dir> <st_number>")
        print("Exemple: python move_st_file.py 01_specs_fonctionnelles 02_specs_techniques 001")
        return
    
    source_dir = sys.argv[1]
    target_dir = sys.argv[2]
    st_number = sys.argv[3]
    
    move_st_file(source_dir, target_dir, st_number)

if __name__ == "__main__":
    main()
