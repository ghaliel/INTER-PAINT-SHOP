#!/usr/bin/env python
"""
Script pour créer un exécutable .exe du projet Django Paint Shop
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_exe():
    """Crée l'exécutable .exe du projet Django"""
    
    # Configuration
    project_name = "paintshop"
    exe_name = "PaintShop.exe"
    
    print("🚀 Début de la création de l'exécutable...")
    
    # Vérifier que PyInstaller est installé
    try:
        import PyInstaller
        print(f"✅ PyInstaller version {PyInstaller.__version__} trouvé")
    except ImportError:
        print("❌ PyInstaller n'est pas installé. Installation...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Créer le fichier spec pour PyInstaller
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('paintshop', 'paintshop'),
        ('store', 'store'),
        ('templates', 'templates'),
        ('static', 'static'),
        ('media', 'media'),
        ('db.sqlite3', '.'),
        ('requirements.txt', '.'),
    ],
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
        'paintshop.settings',
        'paintshop.urls',
        'paintshop.wsgi',
        'paintshop.asgi',
        'jazzmin',
        'django_extensions',
        'crispy_forms',
        'crispy_bootstrap5',
        'PIL',
        'weasyprint',
        'whitenoise',
        'psycopg2',
        'gunicorn',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
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
    with open(f"{project_name}.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    print("📝 Fichier .spec créé")
    
    # Créer l'exécutable avec PyInstaller
    print("🔨 Construction de l'exécutable...")
    result = subprocess.run([
        "pyinstaller",
        "--clean",
        "--onefile",
        f"{project_name}.spec"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Exécutable créé avec succès!")
        print(f"📁 L'exécutable se trouve dans: dist/{exe_name}")
        
        # Copier les fichiers nécessaires dans le dossier dist
        dist_dir = Path("dist")
        if not dist_dir.exists():
            dist_dir.mkdir()
        
        # Copier les fichiers statiques et media si ils existent
        for folder in ["static", "media", "templates"]:
            if Path(folder).exists():
                shutil.copytree(folder, dist_dir / folder, dirs_exist_ok=True)
                print(f"📁 Dossier {folder} copié")
        
        # Copier le fichier de base de données
        if Path("db.sqlite3").exists():
            shutil.copy2("db.sqlite3", dist_dir / "db.sqlite3")
            print("📄 Base de données copiée")
        
        print("\n🎉 Exécutable créé avec succès!")
        print(f"📍 Emplacement: {dist_dir.absolute()}/{exe_name}")
        print("\n📋 Instructions d'utilisation:")
        print("1. Ouvrez un terminal dans le dossier 'dist'")
        print("2. Exécutez: PaintShop.exe runserver")
        print("3. Ouvrez votre navigateur sur: http://127.0.0.1:8000")
        
    else:
        print("❌ Erreur lors de la création de l'exécutable:")
        print(result.stderr)

if __name__ == "__main__":
    create_exe() 