# 🎨 INTER PAINT - Système de Gestion de Peintures

## Description

INTER PAINT est une application web Django complète pour la gestion d'une entreprise de peintures. Le système comprend un site e-commerce pour les clients, un tableau de bord administrateur pour la gestion des produits et commandes, et un système de gestion interne pour le personnel.

## 🚀 Fonctionnalités

### Pour les Clients
- **Catalogue de produits** avec filtrage par catégories et gammes
- **Système de panier** avec gestion des quantités
- **Passation de commandes** avec adresse de livraison
- **Suivi des commandes** en temps réel
- **Historique des commandes** avec possibilité d'annulation
- **Génération de PDF** pour les commandes
- **Formulaire de contact** avec système de tickets
- **Gestion de profil** utilisateur

### Pour le Personnel (Staff)
- **Tableau de bord staff** avec statistiques en temps réel
- **Gestion des produits** (ajout, modification, suppression)
- **Suivi des commandes** avec différents statuts
- **Gestion des stocks** avec alertes automatiques
- **Système de messages internes** (tickets)
- **Planning du personnel**
- **Rapports PDF** détaillés
- **Alertes de stock critique**

### Pour les Super-Administrateurs
- **Tableau de bord super-admin** avec fonctionnalités avancées
- **Impression de toutes les commandes** en PDF
- **Gestion complète du système**
- **Réapprovisionnement automatique**

## 🛠️ Technologies Utilisées

- **Backend**: Django 4.x
- **Base de données**: SQLite (développement) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Génération PDF**: WeasyPrint
- **Authentification**: Django Auth System
- **Envoi d'emails**: Django Email Backend

## 📋 Prérequis

- Python 3.8+
- pip
- Git

## 🔧 Installation

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/inter-paint.git
cd inter-paint
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer la base de données**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Créer un super-utilisateur**
```bash
python manage.py createsuperuser
```

6. **Configurer les paramètres SMTP** (dans `paintshop/settings.py`)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # ou votre serveur SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-application'
DEFAULT_FROM_EMAIL = 'votre-email@gmail.com'
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

## 📁 Structure du Projet

```
inter-paint/
├── paintshop/                 # Configuration principale Django
│   ├── settings.py           # Paramètres du projet
│   ├── urls.py               # URLs principales
│   └── wsgi.py               # Configuration WSGI
├── store/                    # Application principale
│   ├── models.py             # Modèles de données
│   ├── views.py              # Vues et logique métier
│   ├── forms.py              # Formulaires
│   ├── urls.py               # URLs de l'application
│   ├── admin.py              # Configuration admin
│   └── templates/            # Templates HTML
│       ├── store/            # Templates pour les clients
│       └── admin/            # Templates pour l'administration
├── static/                   # Fichiers statiques (CSS, JS, images)
├── media/                    # Fichiers uploadés
├── requirements.txt          # Dépendances Python
└── README.md                 # Ce fichier
```

## 👥 Utilisateurs et Rôles

### Client (Utilisateur standard)
- Accès au catalogue de produits
- Gestion du panier et commandes
- Suivi des commandes
- Contact et support

### Staff (Personnel)
- Tableau de bord avec statistiques
- Gestion des commandes
- Alertes de stock
- Planning du personnel
- Messages internes

### Super-Administrateur
- Toutes les fonctionnalités staff
- Impression de toutes les commandes
- Gestion complète du système
- Réapprovisionnement

## 🎯 Fonctionnalités Clés

### Système de Commandes
- Statuts multiples : Confirmée, En préparation, Expédiée, Livrée, Annulée
- Suivi en temps réel
- Génération automatique de PDF
- Gestion des adresses de livraison

### Gestion des Stocks
- Alertes automatiques pour stock faible
- Système de réapprovisionnement
- Historique des mouvements de stock
- Notifications par email

### Système de Messages
- Tickets de contact automatiques
- Messages internes entre staff
- Alertes de stock critique
- Notifications par email

### Rapports et Analytics
- Rapports PDF détaillés
- Statistiques de vente
- Suivi des performances
- Export de données

## 🔐 Sécurité

- Authentification Django sécurisée
- Protection CSRF sur tous les formulaires
- Validation des données côté serveur
- Gestion des permissions par rôle
- Protection contre les injections SQL

## 📧 Configuration Email

Pour que les emails fonctionnent correctement, configurez les paramètres SMTP dans `paintshop/settings.py` :

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-application'
DEFAULT_FROM_EMAIL = 'votre-email@gmail.com'
```

**Note**: Pour Gmail, utilisez un "mot de passe d'application" si l'authentification à deux facteurs est activée.

## 🚀 Déploiement

### Variables d'environnement
Créez un fichier `.env` à la racine du projet :
```
DEBUG=False
SECRET_KEY=votre-clé-secrète
DATABASE_URL=postgresql://user:password@localhost/dbname
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe
```

### Production
1. Configurer une base de données PostgreSQL
2. Configurer un serveur web (Nginx + Gunicorn)
3. Configurer les variables d'environnement
4. Collecter les fichiers statiques : `python manage.py collectstatic`

## 🐛 Dépannage

### Problèmes courants

1. **Erreur d'envoi d'email**
   - Vérifier la configuration SMTP
   - Vérifier les logs Django

2. **Erreur de génération PDF**
   - Installer WeasyPrint : `pip install weasyprint`
   - Vérifier les dépendances système

3. **Erreur de base de données**
   - Exécuter les migrations : `python manage.py migrate`
   - Vérifier la configuration de la base de données

## 📞 Support

Pour toute question ou problème :
- Email : elasrighali2003@gmail.com
- Téléphone : 06 45 25 01 78
- Adresse : Gueliz, 40000 Marrakech

## 📄 Licence

Ce projet est développé pour INTER PAINT. Tous droits réservés.

## 👨‍💻 Développeur

Développé avec ❤️ pour INTER PAINT

---

**INTER PAINT** - Votre partenaire peinture de confiance à Marrakech