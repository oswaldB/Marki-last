#!/usr/bin/env python3

import os
import sys
import subprocess
import json
from datetime import datetime

# Chemin du fichier de todos
TODO_FILE = ".instructions/todos.json"

# Chemin du script pour lancer le serveur
RUN_SERVER_SCRIPT = "run_serveur"

def load_todos():
    """
    Charge les todos depuis le fichier JSON.
    
    Returns:
        list: Liste des todos.
    """
    if not os.path.exists(TODO_FILE):
        return []
    
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    """
    Sauvegarde les todos dans le fichier JSON.
    
    Args:
        todos (list): Liste des todos à sauvegarder.
    """
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def add_todo(description, agent, priority="medium"):
    """
    Ajoute une nouvelle todo à la liste.
    
    Args:
        description (str): Description de la todo.
        agent (str): Agent responsable de la todo.
        priority (str): Priorité de la todo (low, medium, high).
    """
    todos = load_todos()
    
    todo = {
        "id": len(todos) + 1,
        "description": description,
        "agent": agent,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    todos.append(todo)
    save_todos(todos)
    
    print(f"Todo ajoutée avec succès: {description}")

def update_todo(todo_id, status=None, description=None, agent=None, priority=None):
    """
    Met à jour une todo existante.
    
    Args:
        todo_id (int): ID de la todo à mettre à jour.
        status (str): Nouveau statut de la todo.
        description (str): Nouvelle description de la todo.
        agent (str): Nouveau responsable de la todo.
        priority (str): Nouvelle priorité de la todo.
    """
    todos = load_todos()
    
    for todo in todos:
        if todo["id"] == todo_id:
            if status:
                todo["status"] = status
            if description:
                todo["description"] = description
            if agent:
                todo["agent"] = agent
            if priority:
                todo["priority"] = priority
            
            todo["updated_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_todos(todos)
            
            print(f"Todo mise à jour avec succès: {todo['description']}")
            return
    
    print(f"Erreur: Aucune todo trouvée avec l'ID {todo_id}")

def list_todos():
    """
    Liste toutes les todos.
    """
    todos = load_todos()
    
    if not todos:
        print("Aucune todo trouvée.")
        return
    
    print("\nListe des Todos:")
    print("-" * 80)
    for todo in todos:
        print(f"ID: {todo['id']}")
        print(f"Description: {todo['description']}")
        print(f"Agent: {todo['agent']}")
        print(f"Priorité: {todo['priority']}")
        print(f"Statut: {todo['status']}")
        print(f"Créé le: {todo['created_at']}")
        print(f"Mis à jour le: {todo['updated_at']}")
        print("-" * 80)

def manage_server(action):
    """
    Gère le serveur en fonction de l'action spécifiée.
    
    Args:
        action (str): Action à effectuer (start, stop, restart).
    """
    if action == "start":
        print("Démarrage du serveur...")
        subprocess.run(["python", RUN_SERVER_SCRIPT])
    elif action == "stop":
        print("Arrêt du serveur...")
        # Logique pour arrêter le serveur (à adapter selon votre environnement)
        subprocess.run(["pkill", "-f", RUN_SERVER_SCRIPT])
    elif action == "restart":
        print("Redémarrage du serveur...")
        manage_server("stop")
        manage_server("start")
    else:
        print(f"Erreur: Action non valide: {action}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage_todos_and_server.py <command> [args]")
        print("Commands:")
        print("  add <description> <agent> [priority]")
        print("  update <id> [--status <status>] [--description <description>] [--agent <agent>] [--priority <priority>]")
        print("  list")
        print("  server <action> (start, stop, restart)")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: python manage_todos_and_server.py add <description> <agent> [priority]")
            return
        
        description = sys.argv[2]
        agent = sys.argv[3]
        priority = sys.argv[4] if len(sys.argv) > 4 else "medium"
        
        add_todo(description, agent, priority)
    
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python manage_todos_and_server.py update <id> [--status <status>] [--description <description>] [--agent <agent>] [--priority <priority>]")
            return
        
        todo_id = int(sys.argv[2])
        
        # Parsing des arguments optionnels
        status = None
        description = None
        agent = None
        priority = None
        
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--status" and i + 1 < len(sys.argv):
                status = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--description" and i + 1 < len(sys.argv):
                description = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--agent" and i + 1 < len(sys.argv):
                agent = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--priority" and i + 1 < len(sys.argv):
                priority = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        
        update_todo(todo_id, status, description, agent, priority)
    
    elif command == "list":
        list_todos()
    
    elif command == "server":
        if len(sys.argv) < 3:
            print("Usage: python manage_todos_and_server.py server <action> (start, stop, restart)")
            return
        
        action = sys.argv[2]
        manage_server(action)
    
    else:
        print(f"Erreur: Commande non valide: {command}")

if __name__ == "__main__":
    main()
