# 🚀 Guide de Démarrage - PaintShop Portable

## 📋 Prérequis

- **Windows 10/11** (testé et compatible)
- **Aucune installation** de Python, Django ou base de données requise
- **Navigateur web** (Chrome, Firefox, Edge)

## 🎯 Étapes de Démarrage

### **Méthode 1: Double-clic (Plus Simple)**

1. **Ouvrez l'Explorateur Windows**
2. **Naviguez vers** : `C:\Users\elasr\Paint\dist_portable\`
3. **Double-cliquez** sur `PaintShop_Portable.exe`
4. **Attendez** le démarrage (10-30 secondes)
5. **Ouvrez** votre navigateur sur : **http://127.0.0.1:8000**

### **Méthode 2: Ligne de commande**

#### **Depuis le dossier dist_portable :**
```powershell
cd dist_portable
.\PaintShop_Portable.exe
```

#### **Depuis le répertoire principal :**
```powershell
.\dist_portable\PaintShop_Portable.exe
```

### **Méthode 3: Script batch**

1. **Double-cliquez** sur `Lancer_PaintShop.bat` dans le dossier `dist_portable`
2. **Suivez** les instructions dans la fenêtre de commande

## 🔧 Commandes Utiles

### **Démarrage de base**
```bash
PaintShop_Portable.exe
```

### **Démarrage sur un port spécifique**
```bash
PaintShop_Portable.exe runserver 8080
# Puis ouvrez: http://127.0.0.1:8080
```

### **Vérification du système**
```bash
PaintShop_Portable.exe check
```

### **Aide et commandes disponibles**
```bash
PaintShop_Portable.exe help
```

### **Création d'un super-utilisateur**
```bash
PaintShop_Portable.exe createsuperuser
```

## 🌐 Accès à l'Application

### **Interface Client**
- **URL** : http://127.0.0.1:8000
- **Fonctionnalités** : Catalogue, panier, commandes, profil

### **Interface d'Administration**
- **URL** : http://127.0.0.1:8000/admin
- **Fonctionnalités** : Gestion produits, commandes, utilisateurs

## 🐛 Dépannage

### **Problème : "Le terme n'est pas reconnu"**
**Solution** : Assurez-vous d'être dans le bon dossier ou utilisez le chemin complet
```powershell
.\dist_portable\PaintShop_Portable.exe
```

### **Problème : Port déjà utilisé**
**Solution** : Changez de port
```bash
PaintShop_Portable.exe runserver 8080
```

### **Problème : Application ne démarre pas**
**Solutions** :
1. Vérifiez que tous les fichiers sont présents
2. Désactivez temporairement l'antivirus
3. Exécutez en tant qu'administrateur
4. Vérifiez les permissions du dossier

### **Problème : Navigateur ne se connecte pas**
**Solutions** :
1. Vérifiez que l'application est bien démarrée
2. Essayez : http://localhost:8000
3. Vérifiez votre pare-feu Windows

## 📁 Structure des Fichiers

```
dist_portable/
├── PaintShop_Portable.exe    # Application principale
├── Lancer_PaintShop.bat      # Script de lancement
├── db.sqlite3               # Base de données
└── README.txt               # Documentation
```

## ✅ Vérification du Démarrage

### **Signes de démarrage réussi :**
- Fenêtre de commande affiche "Demarrage du serveur..."
- Message "Ouvrez votre navigateur sur: http://127.0.0.1:8000"
- Pas d'erreur "list index out of range"

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

## 📝 Notes Importantes

- **Application portable** : Aucune installation requise
- **Base de données locale** : Toutes les données restent sur votre machine
- **Fonctionne hors ligne** : Pas besoin de connexion internet
- **Version corrigée** : Plus d'erreur "list index out of range"
- **Sécurisé** : Données locales, pas de transmission externe

## 🆘 Support

En cas de problème :
1. Consultez ce guide de démarrage
2. Vérifiez le fichier `README.txt` dans `dist_portable/`
3. Testez les commandes de dépannage
4. Contactez le support technique

---
**Version** : Portable v1.1 (Corrigée)
**Dernière mise à jour** : 2024
**Statut** : ✅ Prêt à l'utilisation
