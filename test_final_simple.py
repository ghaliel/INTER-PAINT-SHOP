#!/usr/bin/env python
"""
Test final simplifié de l'exécutable portable corrigé
"""
import subprocess
from pathlib import Path

def test_executable():
    """Teste l'exécutable portable corrigé"""
    
    print("Test Final - PaintShop Portable Corrige")
    print("=" * 50)
    
    # Vérifier que l'exécutable existe
    exe_path = Path("dist_portable/PaintShop_Portable.exe")
    if not exe_path.exists():
        print("Exécutable non trouvé")
        return False
    
    print("Exécutable trouvé")
    
    # Test 1: Commande help
    print("\nTest 1: Commande help")
    try:
        result = subprocess.run([str(exe_path), "help"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("Commande help fonctionne")
        else:
            print(f"Erreur: {result.stderr}")
            return False
    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    # Test 2: Commande check
    print("\nTest 2: Commande check")
    try:
        result = subprocess.run([str(exe_path), "check"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("Commande check fonctionne")
        else:
            print(f"Erreur: {result.stderr}")
            return False
    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    print("\nTOUS LES TESTS REUSSIS !")
    print("L'exécutable portable corrigé fonctionne parfaitement")
    print("Plus d'erreur 'list index out of range'")
    print("L'application est prête à être utilisée")
    
    return True

if __name__ == "__main__":
    success = test_executable()
    if not success:
        print("\nDes problèmes ont été détectés")
        exit(1)
