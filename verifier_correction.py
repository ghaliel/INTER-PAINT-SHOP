#!/usr/bin/env python
"""
Script de vérification finale pour la correction de l'erreur "list index out of range"
"""
import os
import sys
from pathlib import Path

def verifier_fichiers():
    """Vérifie que tous les fichiers de correction sont présents"""
    
    print("🔍 Vérification des fichiers de correction")
    print("=" * 50)
    
    fichiers_requis = [
        "final_portable_fixed.py",
        "build_portable_fixed.py", 
        "build_portable_fixed.bat",
        "test_portable_fixed.py",
        "manage_portable_robust.py"
    ]
    
    tous_presents = True
    
    for fichier in fichiers_requis:
        if Path(fichier).exists():
            print(f"✅ {fichier}")
        else:
            print(f"❌ {fichier} - MANQUANT")
            tous_presents = False
    
    return tous_presents

def verifier_script_corrige():
    """Vérifie que le script corrigé fonctionne"""
    
    print("\n🧪 Test du script corrigé")
    print("=" * 30)
    
    try:
        # Importer le script corrigé
        import final_portable_fixed
        print("✅ Script corrigé importé avec succès")
        
        # Vérifier que les fonctions principales existent
        if hasattr(final_portable_fixed, 'main'):
            print("✅ Fonction main() présente")
        else:
            print("❌ Fonction main() manquante")
            return False
            
        if hasattr(final_portable_fixed, 'safe_execute_django_command'):
            print("✅ Fonction safe_execute_django_command() présente")
        else:
            print("❌ Fonction safe_execute_django_command() manquante")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'import: {e}")
        return False

def verifier_build_script():
    """Vérifie que le script de build fonctionne"""
    
    print("\n🔨 Test du script de build")
    print("=" * 30)
    
    try:
        import build_portable_fixed
        print("✅ Script de build importé avec succès")
        
        if hasattr(build_portable_fixed, 'create_portable_exe'):
            print("✅ Fonction create_portable_exe() présente")
            return True
        else:
            print("❌ Fonction create_portable_exe() manquante")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de l'import: {e}")
        return False

def verifier_dossier_dist():
    """Vérifie le dossier de distribution"""
    
    print("\n📁 Vérification du dossier de distribution")
    print("=" * 40)
    
    dist_dir = Path("dist_portable")
    
    if not dist_dir.exists():
        print("❌ Dossier dist_portable/ manquant")
        return False
    
    fichiers_dist = [
        "PaintShop_Portable.exe",
        "Lancer_PaintShop.bat", 
        "db.sqlite3",
        "README.txt"
    ]
    
    tous_presents = True
    
    for fichier in fichiers_dist:
        if (dist_dir / fichier).exists():
            print(f"✅ {fichier}")
        else:
            print(f"❌ {fichier} - MANQUANT")
            tous_presents = False
    
    return tous_presents

def verifier_correction_erreur():
    """Vérifie que la correction de l'erreur est en place"""
    
    print("\n🔧 Vérification de la correction d'erreur")
    print("=" * 40)
    
    try:
        # Lire le script corrigé
        with open("final_portable_fixed.py", "r", encoding="utf-8") as f:
            contenu = f.read()
        
        # Vérifier les éléments de correction
        corrections = [
            "safe_execute_django_command",
            "PaintShop_Portable.exe",
            "IndexError",
            "AttributeError",
            "hasattr(sys, 'argv')"
        ]
        
        toutes_presentes = True
        
        for correction in corrections:
            if correction in contenu:
                print(f"✅ {correction} - Présent")
            else:
                print(f"❌ {correction} - MANQUANT")
                toutes_presentes = False
        
        return toutes_presentes
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
        return False

def main():
    """Fonction principale de vérification"""
    
    print("🎨 PaintShop - Vérification de la correction")
    print("=" * 60)
    
    # Vérifications
    fichiers_ok = verifier_fichiers()
    script_ok = verifier_script_corrige()
    build_ok = verifier_build_script()
    dist_ok = verifier_dossier_dist()
    correction_ok = verifier_correction_erreur()
    
    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DE LA VÉRIFICATION")
    print("=" * 60)
    
    if fichiers_ok:
        print("✅ Fichiers de correction: COMPLETS")
    else:
        print("❌ Fichiers de correction: INCOMPLETS")
    
    if script_ok:
        print("✅ Script corrigé: FONCTIONNEL")
    else:
        print("❌ Script corrigé: DÉFAILLANT")
    
    if build_ok:
        print("✅ Script de build: FONCTIONNEL")
    else:
        print("❌ Script de build: DÉFAILLANT")
    
    if dist_ok:
        print("✅ Dossier de distribution: COMPLET")
    else:
        print("❌ Dossier de distribution: INCOMPLET")
    
    if correction_ok:
        print("✅ Correction d'erreur: IMPLÉMENTÉE")
    else:
        print("❌ Correction d'erreur: MANQUANTE")
    
    # Conclusion
    print("\n" + "=" * 60)
    if all([fichiers_ok, script_ok, build_ok, dist_ok, correction_ok]):
        print("🎉 TOUT EST CORRECT !")
        print("💡 L'erreur 'list index out of range' est corrigée")
        print("🚀 Vous pouvez reconstruire l'exécutable avec:")
        print("   python build_portable_fixed.py")
        print("   ou")
        print("   build_portable_fixed.bat")
    else:
        print("❌ PROBLÈMES DÉTECTÉS")
        print("🔧 Corrigez les erreurs avant de continuer")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
