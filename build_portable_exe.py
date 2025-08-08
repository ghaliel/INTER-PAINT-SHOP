#!/usr/bin/env python
"""
Script pour créer un exécutable portable .exe du projet Django Paint Shop
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_portable_exe():
    """Crée un exécutable portable .exe du projet Django"""
    
    print("🚀 Début de la création de l'exécutable portable...")
    
    # Configuration
    project_name = "paintshop"
    exe_name = "PaintShop_Portable.exe"
    
    # Vérifier que PyInstaller est installé
    try:
        import PyInstaller
        print(f"✅ PyInstaller version {PyInstaller.__version__} trouvé")
    except ImportError:
        print("❌ PyInstaller n'est pas installé. Installation...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Créer le fichier spec pour PyInstaller avec configuration portable
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collecter tous les fichiers nécessaires
datas = [
    ('paintshop', 'paintshop'),
    ('store', 'store'),
    ('db.sqlite3', '.'),
    ('requirements.txt', '.'),
]

# Ajouter les dossiers statiques et media s'ils existent
import os
if os.path.exists('static'):
    datas.append(('static', 'static'))
if os.path.exists('media'):
    datas.append(('media', 'media'))
if os.path.exists('templates'):
    datas.append(('templates', 'templates'))
if os.path.exists('staticfiles'):
    datas.append(('staticfiles', 'staticfiles'))

a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'django',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'store',
        'store.models',
        'store.views',
        'store.urls',
        'store.forms',
        'store.admin',
        'store.apps',
        'paintshop.settings',
        'paintshop.urls',
        'paintshop.wsgi',
        'paintshop.asgi',
        'jazzmin',
        'django_extensions',
        'crispy_forms',
        'crispy_bootstrap5',
        'PIL',
        'PIL._imagingtk',
        'PIL._tkinter_finder',
        'weasyprint',
        'whitenoise',
        'psycopg2',
        'gunicorn',
        'sqlite3',
        'django.db.backends.sqlite3',
        'django.template.loader_tags',
        'django.templatetags.static',
        'django.contrib.admin.templatetags',
        'django.contrib.auth.templatetags',
        'django.contrib.humanize.templatetags',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'IPython',
        'jupyter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{exe_name}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    # Écrire le fichier spec
    with open(f"{project_name}_portable.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    print("📝 Fichier .spec portable créé")
    
    # Créer l'exécutable avec PyInstaller
    print("🔨 Construction de l'exécutable portable...")
    result = subprocess.run([
        "pyinstaller",
        "--clean",
        "--onefile",
        "--distpath", "dist_portable",
        f"{project_name}_portable.spec"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Exécutable portable créé avec succès!")
        
        # Créer le dossier de distribution portable
        dist_dir = Path("dist_portable")
        if not dist_dir.exists():
            dist_dir.mkdir()
        
        # Copier tous les fichiers nécessaires dans le dossier portable
        print("📁 Copie des fichiers nécessaires...")
        
        # Copier les dossiers importants
        folders_to_copy = ["static", "media", "templates", "staticfiles"]
        for folder in folders_to_copy:
            if Path(folder).exists():
                shutil.copytree(folder, dist_dir / folder, dirs_exist_ok=True)
                print(f"📁 Dossier {folder} copié")
        
        # Copier la base de données
        if Path("db.sqlite3").exists():
            shutil.copy2("db.sqlite3", dist_dir / "db.sqlite3")
            print("📄 Base de données copiée")
        
        # Créer un fichier de lancement batch
        batch_content = f'''@echo off
echo ========================================
echo    PaintShop - Application Portable
echo ========================================
echo.
echo 🎨 Démarrage de l'application...
echo 📱 Ouvrez votre navigateur sur: http://127.0.0.1:8000
echo ⏹️  Appuyez sur Ctrl+C pour arrêter
echo.
{exe_name} runserver 127.0.0.1:8000
pause
'''
        
        with open(dist_dir / "Lancer_PaintShop.bat", "w", encoding="utf-8") as f:
            f.write(batch_content)
        
        # Créer un fichier README pour l'utilisateur
        readme_content = '''# 🎨 PaintShop - Application Portable

## 🚀 Comment utiliser

### Méthode 1: Double-clic simple
1. Double-cliquez sur `PaintShop_Portable.exe`
2. L'application se lancera automatiquement
3. Ouvrez votre navigateur sur: http://127.0.0.1:8000

### Méthode 2: Utilisation du fichier batch
1. Double-cliquez sur `Lancer_PaintShop.bat`
2. Suivez les instructions à l'écran

### Méthode 3: Ligne de commande
1. Ouvrez un terminal dans ce dossier
2. Tapez: `PaintShop_Portable.exe runserver`
3. Ouvrez votre navigateur sur: http://127.0.0.1:8000

## 📁 Contenu du dossier

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

**Problème: Port déjà utilisé**
- Changez le port: `PaintShop_Portable.exe runserver 8080`
- Puis ouvrez: http://127.0.0.1:8080

**Problème: Application ne démarre pas**
- Vérifiez que tous les fichiers sont présents
- Essayez de lancer via le fichier .bat

## 📝 Notes

- Cette application est portable et ne nécessite pas d'installation
- Tous les fichiers sont inclus dans ce dossier
- La base de données est locale (SQLite)
- L'application fonctionne hors ligne

## 🔄 Mise à jour

Pour mettre à jour l'application:
1. Remplacez tous les fichiers par les nouveaux
2. Conservez votre base de données si nécessaire
'''
        
        with open(dist_dir / "README.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("\n🎉 Exécutable portable créé avec succès!")
        print(f"📍 Emplacement: {dist_dir.absolute()}")
        print(f"📁 Nom du fichier: {exe_name}")
        print("\n📋 Instructions de distribution:")
        print("1. Copiez tout le contenu du dossier 'dist_portable'")
        print("2. Collez-le sur n'importe quel PC Windows")
        print("3. Double-cliquez sur PaintShop_Portable.exe")
        print("4. L'application fonctionnera immédiatement!")
        
    else:
        print("❌ Erreur lors de la création de l'exécutable:")
        print(result.stderr)

if __name__ == "__main__":
    create_portable_exe() 