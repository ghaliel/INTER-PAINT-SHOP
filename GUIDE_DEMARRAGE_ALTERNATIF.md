# 🚀 Guide de Démarrage Alternatif - PaintShop

## 📋 Solutions de Démarrage

### **Problème Identifié**
L'exécutable portable peut avoir des problèmes avec les commandes Django. Voici des solutions alternatives.

## 🎯 Méthodes de Démarrage

### **Méthode 1: Script Batch Simple (Recommandé)**

1. **Double-cliquez** sur `lancer_simple.bat`
2. **Attendez** le démarrage du serveur
3. **Ouvrez** votre navigateur sur : **http://127.0.0.1:8000**

### **Méthode 2: Ligne de commande avec Python**

#### **Avec environnement virtuel :**
```powershell
# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Lancer l'application
python manage.py runserver 127.0.0.1:8000
```

#### **Sans environnement virtuel :**
```powershell
python manage.py runserver 127.0.0.1:8000
```

### **Méthode 3: Script Python direct**

```powershell
python run_paintshop.py
```

## 🔧 Commandes Utiles

### **Vérification du système**
```bash
python manage.py check
```

### **Création d'un super-utilisateur**
```bash
python manage.py createsuperuser
```

### **Migration de la base de données**
```bash
python manage.py migrate
```

### **Collecte des fichiers statiques**
```bash
python manage.py collectstatic
```

## 🌐 Accès à l'Application

### **Interface Client**
- **URL** : http://127.0.0.1:8000
- **Fonctionnalités** : Catalogue, panier, commandes, profil

### **Interface d'Administration**
- **URL** : http://127.0.0.1:8000/admin
- **Fonctionnalités** : Gestion produits, commandes, utilisateurs

## 🐛 Dépannage

### **Problème : "Module not found"**
**Solution** : Activez l'environnement virtuel
```powershell
.\venv\Scripts\Activate.ps1
```

### **Problème : "Port already in use"**
**Solution** : Changez de port
```bash
python manage.py runserver 8080
```

### **Problème : "Database error"**
**Solution** : Migrez la base de données
```bash
python manage.py migrate
```

### **Problème : "Static files not found"**
**Solution** : Collectez les fichiers statiques
```bash
python manage.py collectstatic
```

## 📁 Structure des Fichiers

```
Paint/
├── manage.py                    # Script de gestion Django
├── run_paintshop.py            # Script de lancement Python
├── lancer_simple.bat           # Script batch de lancement
├── venv/                       # Environnement virtuel
├── paintshop/                  # Configuration Django
├── store/                      # Application principale
├── db.sqlite3                  # Base de données
└── requirements.txt            # Dépendances
```

## ✅ Vérification du Démarrage

### **Signes de démarrage réussi :**
- Message "Starting development server at http://127.0.0.1:8000/"
- Message "Quit the server with CONTROL-C"
- Pas d'erreur de module ou de port

### **Test de connexion :**
1. Ouvrez votre navigateur
2. Allez sur : http://127.0.0.1:8000
3. Vous devriez voir l'interface PaintShop

## 🔄 Arrêt de l'Application

### **Méthode 1: Interface**
- Appuyez sur **Ctrl+C** dans la fenêtre de commande

### **Méthode 2: Fermeture forcée**
- Fermez la fenêtre de commande
- Ou utilisez le Gestionnaire des tâches

## 📝 Avantages de cette Méthode

- **Plus fiable** : Utilise Python directement
- **Plus rapide** : Pas de compilation d'exécutable
- **Plus flexible** : Accès à toutes les commandes Django
- **Plus facile à déboguer** : Messages d'erreur clairs
- **Moins de problèmes** : Pas de problèmes d'encodage ou de modules manquants

## 🆘 Support

En cas de problème :
1. Vérifiez que Python est installé
2. Activez l'environnement virtuel si disponible
3. Installez les dépendances : `pip install -r requirements.txt`
4. Vérifiez la base de données : `python manage.py check`

---
**Version** : Alternative v1.0
**Dernière mise à jour** : 2024
**Statut** : ✅ Solution de contournement fonctionnelle
