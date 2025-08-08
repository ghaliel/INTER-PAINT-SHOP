#!/usr/bin/env python
"""
Script de test pour la version corrigée de l'exécutable portable
"""
import os
import sys
from pathlib import Path

def test_portable_script():
    """Teste le script portable corrigé"""
    
    print("🧪 Test de la version corrigée PaintShop Portable")
    print("=" * 50)
    
    # Simuler l'environnement de l'exécutable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintshop.settings')
    os.environ.setdefault('DEBUG', 'False')
    os.environ.setdefault('ALLOWED_HOSTS', 'localhost,127.0.0.1')
    
    # Ajouter le répertoire courant au PYTHONPATH
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    # Importer et tester le script corrigé
    try:
        # Simuler différents scénarios d'arguments
        test_cases = [
            [],  # Aucun argument
            ['runserver'],  # Commande runserver
            ['runserver', '8080'],  # Commande avec port
            ['migrate'],  # Commande migrate
            ['help'],  # Commande d'aide
        ]
        
        for i, args in enumerate(test_cases, 1):
            print(f"\n🧪 Test {i}: Arguments = {args}")
            
            # Sauvegarder les arguments originaux
            original_argv = sys.argv.copy()
            
            try:
                # Simuler les arguments
                sys.argv = ['PaintShop_Portable.exe'] + args
                
                # Importer et exécuter le script corrigé
                from final_portable_fixed import main
                main()
                
                print(f"✅ Test {i} réussi")
                
            except Exception as e:
                print(f"❌ Test {i} échoué: {e}")
            
            finally:
                # Restaurer les arguments originaux
                sys.argv = original_argv
        
        print("\n🎉 Tous les tests terminés!")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

if __name__ == "__main__":
    success = test_portable_script()
    if not success:
        sys.exit(1)
