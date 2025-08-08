#!/usr/bin/env python
"""
Script de vérification des prérequis pour PaintShop Portable
"""
import os
import sys
import platform
import psutil
import subprocess
from pathlib import Path

def verifier_systeme():
    """Vérifie les prérequis système"""
    
    print("🔍 Vérification des prérequis système...")
    print("=" * 50)
    
    # Vérifier le système d'exploitation
    systeme = platform.system()
    version = platform.version()
    architecture = platform.architecture()[0]
    
    print(f"🖥️  Système d'exploitation: {systeme} {version}")
    print(f"🏗️  Architecture: {architecture}")
    
    if systeme != "Windows":
        print("❌ ERREUR: Windows requis")
        return False
    
    # Vérifier la version de Windows
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        version_windows = winreg.QueryValueEx(key, "CurrentVersion")[0]
        build = winreg.QueryValueEx(key, "CurrentBuild")[0]
        print(f"📋 Version Windows: {version_windows} (Build {build})")
        
        if float(version_windows) < 10.0:
            print("⚠️  ATTENTION: Windows 10 ou plus récent recommandé")
    except:
        print("ℹ️  Version Windows: Non détectée")
    
    # Vérifier la RAM
    ram_gb = psutil.virtual_memory().total / (1024**3)
    print(f"💾 RAM: {ram_gb:.1f} GB")
    
    if ram_gb < 4:
        print("❌ ERREUR: Minimum 4 GB RAM requis")
        return False
    elif ram_gb < 8:
        print("⚠️  ATTENTION: 8 GB RAM recommandés")
    
    # Vérifier l'espace disque
    disque = psutil.disk_usage('.')
    espace_gb = disque.free / (1024**3)
    print(f"💿 Espace disque libre: {espace_gb:.1f} GB")
    
    if espace_gb < 0.2:
        print("❌ ERREUR: Minimum 200 MB d'espace libre requis")
        return False
    elif espace_gb < 0.5:
        print("⚠️  ATTENTION: 500 MB d'espace libre recommandés")
    
    return True

def verifier_fichiers():
    """Vérifie la présence des fichiers nécessaires"""
    
    print("\n📁 Vérification des fichiers...")
    
    fichiers_requis = [
        "PaintShop_Portable.exe",
        "Lancer_PaintShop.bat",
        "README.txt",
        "db.sqlite3"
    ]
    
    dossiers_requis = [
        "static",
        "media"
    ]
    
    fichiers_manquants = []
    
    for fichier in fichiers_requis:
        if Path(fichier).exists():
            taille = Path(fichier).stat().st_size / (1024**2)
            print(f"✅ {fichier} ({taille:.1f} MB)")
        else:
            print(f"❌ {fichier} - MANQUANT")
            fichiers_manquants.append(fichier)
    
    for dossier in dossiers_requis:
        if Path(dossier).exists():
            print(f"✅ {dossier}/")
        else:
            print(f"⚠️  {dossier}/ - Optionnel")
    
    if fichiers_manquants:
        print(f"\n❌ Fichiers manquants: {', '.join(fichiers_manquants)}")
        return False
    
    return True

def verifier_reseau():
    """Vérifie la configuration réseau"""
    
    print("\n🌐 Vérification réseau...")
    
    # Vérifier le port 8000
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 8000))
        sock.close()
        
        if result == 0:
            print("⚠️  Port 8000 déjà utilisé")
            print("💡 Solution: Utilisez un autre port (ex: 8080)")
        else:
            print("✅ Port 8000 disponible")
    except:
        print("ℹ️  Vérification du port: Impossible")
    
    return True

def verifier_navigateur():
    """Vérifie la présence d'un navigateur"""
    
    print("\n🌍 Vérification navigateur...")
    
    navigateurs = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    
    navigateur_trouve = False
    
    for navigateur in navigateurs:
        if Path(navigateur).exists():
            print(f"✅ Navigateur trouvé: {Path(navigateur).name}")
            navigateur_trouve = True
            break
    
    if not navigateur_trouve:
        print("⚠️  Aucun navigateur détecté")
        print("💡 Installez Chrome, Firefox ou Edge")
    
    return navigateur_trouve

def verifier_antivirus():
    """Vérifie les paramètres antivirus"""
    
    print("\n🛡️  Vérification antivirus...")
    
    # Vérifier si Windows Defender est actif
    try:
        result = subprocess.run(['powershell', 'Get-MpComputerStatus'], 
                              capture_output=True, text=True, timeout=10)
        if 'RealTimeProtectionEnabled : True' in result.stdout:
            print("⚠️  Windows Defender actif")
            print("💡 Ajoutez le dossier à la liste blanche si nécessaire")
        else:
            print("✅ Windows Defender: Non détecté ou désactivé")
    except:
        print("ℹ️  Vérification antivirus: Impossible")
    
    return True

def main():
    """Fonction principale"""
    
    print("🎨 PaintShop - Vérification des prérequis")
    print("=" * 50)
    
    # Vérifications
    systeme_ok = verifier_systeme()
    fichiers_ok = verifier_fichiers()
    reseau_ok = verifier_reseau()
    navigateur_ok = verifier_navigateur()
    antivirus_ok = verifier_antivirus()
    
    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES VÉRIFICATIONS")
    print("=" * 50)
    
    if systeme_ok:
        print("✅ Système: Compatible")
    else:
        print("❌ Système: Incompatible")
    
    if fichiers_ok:
        print("✅ Fichiers: Complets")
    else:
        print("❌ Fichiers: Incomplets")
    
    if reseau_ok:
        print("✅ Réseau: OK")
    else:
        print("❌ Réseau: Problème")
    
    if navigateur_ok:
        print("✅ Navigateur: Trouvé")
    else:
        print("⚠️  Navigateur: Non trouvé")
    
    if antivirus_ok:
        print("✅ Antivirus: Vérifié")
    else:
        print("⚠️  Antivirus: Non vérifié")
    
    # Conclusion
    print("\n" + "=" * 50)
    if systeme_ok and fichiers_ok:
        print("🎉 PRÊT À LANCER !")
        print("💡 Double-cliquez sur PaintShop_Portable.exe")
        print("🌐 Ouvrez http://127.0.0.1:8000 dans votre navigateur")
    else:
        print("❌ PROBLÈMES DÉTECTÉS")
        print("🔧 Corrigez les erreurs avant de lancer l'application")
    
    print("=" * 50)

if __name__ == "__main__":
    main() 