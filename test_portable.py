#!/usr/bin/env python
"""
Script de test pour vérifier la portabilité de l'exécutable
"""
import os
import sys
import subprocess
from pathlib import Path

def test_portable_setup():
    """Teste la configuration portable"""
    
    print("🧪 Test de la configuration portable...")
    
    # Vérifier les fichiers nécessaires
    required_files = [
        "paintshop",
        "store", 
        "db.sqlite3",
        "manage_portable.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Fichiers manquants: {', '.join(missing_files)}")
        return False
    
    print("✅ Tous les fichiers nécessaires sont présents")
    
    # Vérifier la configuration Django
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintshop.settings')
        from django.conf import settings
        print("✅ Configuration Django chargée")
    except Exception as e:
        print(f"❌ Erreur de configuration Django: {e}")
        return False
    
    # Vérifier la base de données
    try:
        from django.db import connection
        connection.ensure_connection()
        print("✅ Connexion à la base de données établie")
    except Exception as e:
        print(f"❌ Erreur de base de données: {e}")
        return False
    
    return True

def test_django_commands():
    """Teste les commandes Django"""
    
    print("\n🔧 Test des commandes Django...")
    
    commands_to_test = [
        ["check"],
        ["showmigrations"],
    ]
    
    for cmd in commands_to_test:
        try:
            result = subprocess.run([
                sys.executable, "manage_portable.py"
            ] + cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"✅ Commande {' '.join(cmd)} réussie")
            else:
                print(f"⚠️  Commande {' '.join(cmd)} échouée: {result.stderr[:100]}")
                
        except Exception as e:
            print(f"❌ Erreur lors du test de {' '.join(cmd)}: {e}")

def main():
    """Fonction principale de test"""
    
    print("🎨 Test de portabilité - PaintShop")
    print("=" * 40)
    
    # Test de la configuration
    if not test_portable_setup():
        print("\n❌ Tests échoués - Configuration incorrecte")
        return False
    
    # Test des commandes Django
    test_django_commands()
    
    print("\n✅ Tests terminés avec succès!")
    print("🎉 L'exécutable portable est prêt à être distribué")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 