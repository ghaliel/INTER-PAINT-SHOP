#!/usr/bin/env python
"""
Script de lancement pour l'exécutable PaintShop
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    """Lance l'application Django PaintShop"""
    
    # Définir les variables d'environnement
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintshop.settings')
    os.environ.setdefault('DEBUG', 'False')
    
    # Ajouter le répertoire courant au PYTHONPATH
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    # Vérifier si des arguments sont passés
    if len(sys.argv) > 1:
        # Passer les arguments à Django
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    else:
        # Par défaut, lancer le serveur de développement
        print("🎨 PaintShop - Application de vente de peintures")
        print("🚀 Démarrage du serveur...")
        print("📱 Ouvrez votre navigateur sur: http://127.0.0.1:8000")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter le serveur")
        print("-" * 50)
        
        # Lancer le serveur Django
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])

if __name__ == '__main__':
    main() 