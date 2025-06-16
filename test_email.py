#!/usr/bin/env python
"""
Script de test pour vérifier la configuration email
"""
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintshop.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email_configuration():
    """Test de la configuration email"""
    print("=== Test de la configuration email ===")
    print(f"EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
    print()
    
    try:
        # Test d'envoi d'email
        print("Tentative d'envoi d'email de test...")
        send_mail(
            subject='Test de configuration email - INTER PAINT',
            message='Ceci est un email de test pour vérifier la configuration email de votre site INTER PAINT.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['elasrighali2003@gmail.com'],
            fail_silently=False,
        )
        print("✅ Email envoyé avec succès !")
        print("Vérifiez votre boîte de réception Gmail.")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi d'email: {e}")
        print()
        print("=== Solutions possibles ===")
        print("1. Vérifiez que l'authentification à deux facteurs est activée sur votre compte Gmail")
        print("2. Créez un mot de passe d'application spécifique pour Django")
        print("3. Remplacez EMAIL_HOST_PASSWORD dans settings.py par le mot de passe d'application")
        print()
        print("Pour créer un mot de passe d'application Gmail:")
        print("1. Allez sur https://myaccount.google.com/security")
        print("2. Activez l'authentification à deux facteurs si ce n'est pas fait")
        print("3. Cliquez sur 'Mots de passe d'application'")
        print("4. Sélectionnez 'Application' et entrez 'Django'")
        print("5. Copiez le mot de passe généré et mettez-le dans settings.py")

if __name__ == '__main__':
    test_email_configuration() 