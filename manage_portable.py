#!/usr/bin/env python
"""
Script de gestion pour l'exécutable portable PaintShop
"""
import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Configure l'environnement pour l'exécutable portable"""
    
    # Définir les variables d'environnement
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintshop.settings')
    os.environ.setdefault('DEBUG', 'False')
    os.environ.setdefault('ALLOWED_HOSTS', 'localhost,127.0.0.1')
    
    # Ajouter le répertoire courant au PYTHONPATH
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    # Vérifier si la base de données existe
    db_path = current_dir / "db.sqlite3"
    if not db_path.exists():
        print("⚠️  Base de données non trouvée. Création d'une nouvelle base...")
        try:
            from django.core.management import execute_from_command_line
            # Utiliser sys.argv[0] au lieu de 'manage.py'
            execute_from_command_line([sys.argv[0], 'migrate'])
            print("✅ Base de données créée avec succès")
        except Exception as e:
            print(f"❌ Erreur lors de la création de la base: {e}")

def main():
    """Point d'entrée principal pour l'exécutable portable"""
    
    print("🎨 PaintShop - Application Portable")
    print("=" * 50)
    
    # Configuration de l'environnement
    setup_environment()
    
    # Vérifier les arguments
    if len(sys.argv) > 1:
        # Passer les arguments à Django
        try:
            from django.core.management import execute_from_command_line
            execute_from_command_line(sys.argv)
        except Exception as e:
            print(f"❌ Erreur: {e}")
            input("Appuyez sur Entrée pour continuer...")
    else:
        # Lancement par défaut
        print("🚀 Démarrage du serveur...")
        print("📱 Ouvrez votre navigateur sur: http://127.0.0.1:8000")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter le serveur")
        print("-" * 50)
        
        try:
            from django.core.management import execute_from_command_line
            # Utiliser sys.argv[0] au lieu de 'manage.py'
            execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])
        except KeyboardInterrupt:
            print("\n👋 Application arrêtée par l'utilisateur")
        except Exception as e:
            print(f"❌ Erreur lors du démarrage: {e}")
            input("Appuyez sur Entrée pour continuer...")

if __name__ == '__main__':
    main() 