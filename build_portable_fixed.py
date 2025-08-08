#!/usr/bin/env python
"""
Script de build pour créer l'exécutable portable PaintShop avec la version corrigée
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_portable_exe():
    """Crée l'exécutable portable avec la version corrigée"""
    
    print("🎨 PaintShop - Création de l'exécutable portable (version corrigée)")
    print("=" * 60)
    
    # Vérifier PyInstaller
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} trouvé")
    except ImportError:
        print("❌ PyInstaller non trouvé")
        print("💡 Installez-le avec: pip install pyinstaller")
        return False
    
    # Créer le dossier de distribution
    dist_dir = Path("dist_portable")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    print("🔨 Création de l'exécutable...")
    
    # Commande PyInstaller optimisée avec le script corrigé
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
        "--hidden-import=django.db.backends.sqlite3",
        "--hidden-import=django.core.management",
        "--hidden-import=django.core.management.commands.runserver",
        "--hidden-import=django.core.management.commands.migrate",
        "--hidden-import=django.core.management.commands.collectstatic",
        "--hidden-import=django.core.management.commands.createsuperuser",
        "--hidden-import=django.core.management.commands.check",
        "--hidden-import=django.core.management.commands.help",
        "--hidden-import=django.core.management.commands.shell",
        "--hidden-import=django.core.management.commands.startapp",
        "--hidden-import=django.core.management.commands.startproject",
        "--hidden-import=django.core.management.commands.test",
        "--hidden-import=django.core.management.commands.testserver",
        "--hidden-import=django.core.management.commands.dumpdata",
        "--hidden-import=django.core.management.commands.loaddata",
        "--hidden-import=django.core.management.commands.flush",
        "--hidden-import=django.core.management.commands.inspectdb",
        "--hidden-import=django.core.management.commands.makemigrations",
        "--hidden-import=django.core.management.commands.showmigrations",
        "--hidden-import=django.core.management.commands.sqlflush",
        "--hidden-import=django.core.management.commands.sqlmigrate",
        "--hidden-import=django.core.management.commands.sqlsequencereset",
        "--hidden-import=django.core.management.commands.squashmigrations",
        "--hidden-import=django.core.management.commands.optimizemigration",
        "--hidden-import=django.core.management.commands.sendtestemail",
        "--hidden-import=django.core.management.commands.compilemessages",
        "--hidden-import=django.core.management.commands.makemessages",
        "--hidden-import=django.core.management.commands.createcachetable",
        "--hidden-import=django.core.management.commands.dbshell",
        "--hidden-import=django.core.management.commands.diffsettings",
        "--hidden-import=django.core.management.commands.findstatic",
        "--hidden-import=django.core.management.commands.clearsessions",
        "--hidden-import=django.core.management.commands.remove_stale_contenttypes",
        "--hidden-import=django.core.management.commands.changepassword",
        "--hidden-import=django_extensions.management.commands",
        "--hidden-import=django_extensions.management.commands.shell_plus",
        "--hidden-import=django_extensions.management.commands.runserver_plus",
        "--hidden-import=django_extensions.management.commands.runscript",
        "--hidden-import=django_extensions.management.commands.notes",
        "--hidden-import=django_extensions.management.commands.print_settings",
        "--hidden-import=django_extensions.management.commands.print_user_for_session",
        "--hidden-import=django_extensions.management.commands.raise_test_exception",
        "--hidden-import=django_extensions.management.commands.reset_db",
        "--hidden-import=django_extensions.management.commands.reset_schema",
        "--hidden-import=django_extensions.management.commands.runjob",
        "--hidden-import=django_extensions.management.commands.runjobs",
        "--hidden-import=django_extensions.management.commands.runprofileserver",
        "--hidden-import=django_extensions.management.commands.set_default_site",
        "--hidden-import=django_extensions.management.commands.set_fake_emails",
        "--hidden-import=django_extensions.management.commands.set_fake_passwords",
        "--hidden-import=django_extensions.management.commands.show_permissions",
        "--hidden-import=django_extensions.management.commands.show_template_tags",
        "--hidden-import=django_extensions.management.commands.show_urls",
        "--hidden-import=django_extensions.management.commands.sqlcreate",
        "--hidden-import=django_extensions.management.commands.sqldiff",
        "--hidden-import=django_extensions.management.commands.sqldsn",
        "--hidden-import=django_extensions.management.commands.sync_s3",
        "--hidden-import=django_extensions.management.commands.syncdata",
        "--hidden-import=django_extensions.management.commands.unreferenced_files",
        "--hidden-import=django_extensions.management.commands.update_permissions",
        "--hidden-import=django_extensions.management.commands.validate_templates",
        "--hidden-import=django_extensions.management.commands.admin_generator",
        "--hidden-import=django_extensions.management.commands.clean_pyc",
        "--hidden-import=django_extensions.management.commands.clear_cache",
        "--hidden-import=django_extensions.management.commands.compile_pyc",
        "--hidden-import=django_extensions.management.commands.create_command",
        "--hidden-import=django_extensions.management.commands.create_jobs",
        "--hidden-import=django_extensions.management.commands.create_template_tags",
        "--hidden-import=django_extensions.management.commands.delete_squashed_migrations",
        "--hidden-import=django_extensions.management.commands.describe_form",
        "--hidden-import=django_extensions.management.commands.drop_test_database",
        "--hidden-import=django_extensions.management.commands.dumpscript",
        "--hidden-import=django_extensions.management.commands.export_emails",
        "--hidden-import=django_extensions.management.commands.find_template",
        "--hidden-import=django_extensions.management.commands.generate_password",
        "--hidden-import=django_extensions.management.commands.generate_secret_key",
        "--hidden-import=django_extensions.management.commands.graph_models",
        "--hidden-import=django_extensions.management.commands.list_model_info",
        "--hidden-import=django_extensions.management.commands.list_signals",
        "--hidden-import=django_extensions.management.commands.mail_debug",
        "--hidden-import=django_extensions.management.commands.managestate",
        "--hidden-import=django_extensions.management.commands.merge_model_instances",
        "--hidden-import=django_extensions.management.commands.print_settings",
        "--hidden-import=django_extensions.management.commands.print_user_for_session",
        "--hidden-import=django_extensions.management.commands.raise_test_exception",
        "--hidden-import=django_extensions.management.commands.reset_db",
        "--hidden-import=django_extensions.management.commands.reset_schema",
        "--hidden-import=django_extensions.management.commands.runjob",
        "--hidden-import=django_extensions.management.commands.runjobs",
        "--hidden-import=django_extensions.management.commands.runprofileserver",
        "--hidden-import=django_extensions.management.commands.runscript",
        "--hidden-import=django_extensions.management.commands.runserver_plus",
        "--hidden-import=django_extensions.management.commands.set_default_site",
        "--hidden-import=django_extensions.management.commands.set_fake_emails",
        "--hidden-import=django_extensions.management.commands.set_fake_passwords",
        "--hidden-import=django_extensions.management.commands.shell_plus",
        "--hidden-import=django_extensions.management.commands.show_permissions",
        "--hidden-import=django_extensions.management.commands.show_template_tags",
        "--hidden-import=django_extensions.management.commands.show_urls",
        "--hidden-import=django_extensions.management.commands.sqlcreate",
        "--hidden-import=django_extensions.management.commands.sqldiff",
        "--hidden-import=django_extensions.management.commands.sqldsn",
        "--hidden-import=django_extensions.management.commands.sync_s3",
        "--hidden-import=django_extensions.management.commands.syncdata",
        "--hidden-import=django_extensions.management.commands.unreferenced_files",
        "--hidden-import=django_extensions.management.commands.update_permissions",
        "--hidden-import=django_extensions.management.commands.validate_templates",
        "--hidden-import=store.management.commands.add_categories",
        "--hidden-import=store.management.commands.add_gamme_data",
        "--hidden-import=store.management.commands.setup_test_data",
        "final_portable_fixed.py"  # Utiliser la version corrigée
    ]
    
    # Ajouter les dossiers s'ils existent
    for folder in ["static", "media", "templates", "staticfiles"]:
        if Path(folder).exists():
            cmd.append(f"--add-data={folder};{folder}")
            print(f"📁 Ajout du dossier: {folder}")
    
    try:
        print("⏳ Création en cours (cela peut prendre 5-10 minutes)...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        
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
            print("📝 Fichier batch de lancement créé")
            
            print("\n🎉 Exécutable portable créé avec succès!")
            print(f"📍 Emplacement: {dist_dir.absolute()}")
            print("\n📋 Instructions de distribution:")
            print("1. Copiez tout le contenu du dossier 'dist_portable'")
            print("2. Collez-le sur n'importe quel PC Windows")
            print("3. Double-cliquez sur PaintShop_Portable.exe")
            print("4. L'application fonctionnera immédiatement!")
            
            return True
            
        else:
            print("❌ Erreur lors de la création:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Timeout - Le processus a pris trop de temps")
        return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    success = create_portable_exe()
    if not success:
        sys.exit(1)
