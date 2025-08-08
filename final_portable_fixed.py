#!/usr/bin/env python
"""
Script de gestion ultra-robuste pour l'exécutable portable PaintShop
Version corrigée pour éviter l'erreur "list index out of range"
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
            print("Base de donnees non trouvee. Creation d'une nouvelle base...")
            try:
                from django.core.management import execute_from_command_line
                # Utiliser un nom de script fixe et sécurisé
                execute_from_command_line(['PaintShop_Portable.exe', 'migrate'])
                print("Base de donnees creee avec succes")
            except Exception as e:
                print(f"Erreur lors de la creation de la base: {e}")
                print("La base de donnees sera creee automatiquement au premier lancement")
    except Exception as e:
        print(f"Erreur lors de la configuration: {e}")

def safe_execute_django_command(command_args):
    """Exécute une commande Django de manière sécurisée"""
    try:
        from django.core.management import execute_from_command_line
        # Utiliser un nom de script fixe pour éviter les erreurs d'index
        safe_args = ['PaintShop_Portable.exe'] + command_args
        execute_from_command_line(safe_args)
        return True
    except Exception as e:
        print(f"Erreur lors de l'execution: {e}")
        return False
    
def main():
    """Point d'entrée principal pour l'exécutable portable"""
    
    print("PaintShop - Application Portable")
    print("=" * 50)
    
    # Configuration de l'environnement
    setup_environment()
    
    # Vérifier les arguments de manière ultra-sécurisée
    try:
        # Récupérer les arguments de manière sécurisée
        args = []
        try:
            if hasattr(sys, 'argv') and sys.argv:
                args = sys.argv[1:]  # Ignorer le nom du script
        except (IndexError, AttributeError):
            args = []
        
        if args:
            # Passer les arguments à Django
            print(f"Execution de la commande: {' '.join(args)}")
            if not safe_execute_django_command(args):
                print("Essayez de relancer l'application")
                input("Appuyez sur Entree pour continuer...")
        else:
            # Lancement par défaut
            print("Demarrage du serveur...")
            print("Ouvrez votre navigateur sur: http://127.0.0.1:8000")
            print("Appuyez sur Ctrl+C pour arreter le serveur")
            print("-" * 50)
            
            try:
                if not safe_execute_django_command(['runserver', '127.0.0.1:8000']):
                    print("Solutions possibles:")
                    print("   1. Verifiez que tous les fichiers sont presents")
                    print("   2. Desactivez temporairement l'antivirus")
                    print("   3. Executez en tant qu'administrateur")
                    print("   4. Verifiez que le port 8000 n'est pas utilise")
                    input("Appuyez sur Entree pour continuer...")
            except KeyboardInterrupt:
                print("\nApplication arretee par l'utilisateur")
            except Exception as e:
                print(f"Erreur lors du demarrage: {e}")
                print("Solutions possibles:")
                print("   1. Verifiez que tous les fichiers sont presents")
                print("   2. Desactivez temporairement l'antivirus")
                print("   3. Executez en tant qu'administrateur")
                print("   4. Verifiez que le port 8000 n'est pas utilise")
                input("Appuyez sur Entree pour continuer...")
    except Exception as e:
        print(f"Erreur critique: {e}")
        print("L'application ne peut pas demarrer")
        input("Appuyez sur Entree pour continuer...")

if __name__ == '__main__':
    main() 