#!/usr/bin/env python
"""
Script de gestion robuste pour l'exécutable portable PaintShop
"""
import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Configure l'environnement pour l'exécutable portable"""
    
    try:
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
                # Utiliser le nom du script actuel
                script_name = os.path.basename(sys.argv[0])
                execute_from_command_line([script_name, 'migrate'])
                print("✅ Base de données créée avec succès")
            except Exception as e:
                print(f"❌ Erreur lors de la création de la base: {e}")
                print("💡 La base de données sera créée automatiquement au premier lancement")
    except Exception as e:
        print(f"⚠️  Erreur lors de la configuration: {e}")

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
            print("💡 Essayez de relancer l'application")
            input("Appuyez sur Entrée pour continuer...")
    else:
        # Lancement par défaut
        print("🚀 Démarrage du serveur...")
        print("📱 Ouvrez votre navigateur sur: http://127.0.0.1:8000")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter le serveur")
        print("-" * 50)
        
        try:
            from django.core.management import execute_from_command_line
            # Utiliser le nom du script actuel
            script_name = os.path.basename(sys.argv[0])
            execute_from_command_line([script_name, 'runserver', '127.0.0.1:8000'])
        except KeyboardInterrupt:
            print("\n👋 Application arrêtée par l'utilisateur")
        except Exception as e:
            print(f"❌ Erreur lors du démarrage: {e}")
            print("💡 Solutions possibles:")
            print("   1. Vérifiez que tous les fichiers sont présents")
            print("   2. Désactivez temporairement l'antivirus")
            print("   3. Exécutez en tant qu'administrateur")
            print("   4. Vérifiez que le port 8000 n'est pas utilisé")
            input("Appuyez sur Entrée pour continuer...")

if __name__ == '__main__':
    main() 