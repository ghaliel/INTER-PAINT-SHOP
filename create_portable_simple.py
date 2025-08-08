#!/usr/bin/env python
"""
Script simplifié pour créer un exécutable portable PaintShop
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    """Crée l'exécutable portable"""
    
    print("🎨 PaintShop - Création de l'exécutable portable")
    print("=" * 50)
    
    # Vérifier Python
    try:
        import PyInstaller
        print(f"✅ PyInstaller trouvé (version {PyInstaller.__version__})")
    except ImportError:
        print("📦 Installation de PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Créer le dossier de distribution
    dist_dir = Path("dist_portable")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    print("🔨 Création de l'exécutable...")
    
    # Commande PyInstaller simplifiée
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name=PaintShop_Portable",
        "--distpath=dist_portable",
        "--add-data=paintshop;paintshop",
        "--add-data=store;store",
        "--add-data=db.sqlite3;.",
        "--hidden-import=django",
        "--hidden-import=django.contrib.admin",
        "--hidden-import=django.contrib.auth",
        "--hidden-import=django.contrib.contenttypes",
        "--hidden-import=django.contrib.sessions",
        "--hidden-import=django.contrib.messages",
        "--hidden-import=django.contrib.staticfiles",
        "--hidden-import=store",
        "--hidden-import=store.models",
        "--hidden-import=store.views",
        "--hidden-import=store.urls",
        "--hidden-import=store.forms",
        "--hidden-import=store.admin",
        "--hidden-import=paintshop.settings",
        "--hidden-import=paintshop.urls",
        "--hidden-import=paintshop.wsgi",
        "--hidden-import=jazzmin",
        "--hidden-import=django_extensions",
        "--hidden-import=crispy_forms",
        "--hidden-import=crispy_bootstrap5",
        "--hidden-import=PIL",
        "--hidden-import=weasyprint",
        "--hidden-import=whitenoise",
        "--hidden-import=sqlite3",
        "manage_portable.py"
    ]
    
    # Ajouter les dossiers s'ils existent
    for folder in ["static", "media", "templates", "staticfiles"]:
        if Path(folder).exists():
            cmd.append(f"--add-data={folder};{folder}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print("✅ Exécutable créé avec succès!")
            
            # Copier les fichiers supplémentaires
            print("📁 Copie des fichiers supplémentaires...")
            
            # Copier la base de données
            if Path("db.sqlite3").exists():
                shutil.copy2("db.sqlite3", dist_dir / "db.sqlite3")
                print("📄 Base de données copiée")
            
            # Créer le fichier batch de lancement
            batch_content = '''@echo off
echo ========================================
echo    PaintShop - Application Portable
echo ========================================
echo.
echo 🎨 Démarrage de l'application...
echo 📱 Ouvrez votre navigateur sur: http://127.0.0.1:8000
echo ⏹️  Appuyez sur Ctrl+C pour arrêter
echo.
PaintShop_Portable.exe runserver 127.0.0.1:8000
pause
'''
            
            with open(dist_dir / "Lancer_PaintShop.bat", "w", encoding="utf-8") as f:
                f.write(batch_content)
            
            # Créer le README
            readme_content = '''# 🎨 PaintShop - Application Portable

## 🚀 Utilisation

1. **Double-cliquez** sur `PaintShop_Portable.exe`
2. L'application se lance automatiquement
3. Ouvrez votre navigateur sur: http://127.0.0.1:8000

## 📁 Contenu

- `PaintShop_Portable.exe` - Application principale
- `Lancer_PaintShop.bat` - Script de lancement
- `db.sqlite3` - Base de données
- `static/` - Fichiers statiques
- `media/` - Fichiers média
- `templates/` - Templates Django

## 🔧 Fonctionnalités

✅ Interface d'administration
✅ Gestion des produits
✅ Système de panier
✅ Gestion des commandes
✅ Système d'authentification
✅ Génération de PDF
✅ Gestion des images

## 🐛 Dépannage

**Port déjà utilisé**: `PaintShop_Portable.exe runserver 8080`
**Application ne démarre pas**: Vérifiez que tous les fichiers sont présents

## 📝 Notes

- Application portable - aucune installation requise
- Base de données locale (SQLite)
- Fonctionne hors ligne
'''
            
            with open(dist_dir / "README.txt", "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            print("\n🎉 Exécutable portable créé avec succès!")
            print(f"📍 Emplacement: {dist_dir.absolute()}")
            print("\n📋 Instructions de distribution:")
            print("1. Copiez tout le contenu du dossier 'dist_portable'")
            print("2. Collez-le sur n'importe quel PC Windows")
            print("3. Double-cliquez sur PaintShop_Portable.exe")
            print("4. L'application fonctionnera immédiatement!")
            
        else:
            print("❌ Erreur lors de la création:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⏰ Timeout - Le processus a pris trop de temps")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main() 