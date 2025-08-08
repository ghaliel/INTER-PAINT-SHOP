# 🎨 PaintShop - Création de l'Exécutable

Ce guide explique comment créer un fichier exécutable (.exe) pour votre application Django PaintShop.

## 📋 Prérequis

- Python 3.8 ou supérieur
- Windows 10/11
- Toutes les dépendances du projet installées

## 🚀 Création de l'Exécutable

### Méthode 1: Utilisation du script batch (Recommandé)

1. **Double-cliquez** sur le fichier `build_exe.bat`
2. Attendez que le processus se termine
3. L'exécutable sera créé dans le dossier `dist/`

### Méthode 2: Utilisation manuelle

1. **Ouvrez un terminal** dans le dossier du projet
2. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancez le script de création** :
   ```bash
   python build_exe.py
   ```

## 📁 Structure après création

```
dist/
├── PaintShop.exe          # Exécutable principal
├── db.sqlite3            # Base de données
├── static/               # Fichiers statiques
├── media/                # Fichiers média
└── templates/            # Templates Django
```

## 🎯 Utilisation de l'Exécutable

### Lancement simple
1. **Double-cliquez** sur `PaintShop.exe` dans le dossier `dist/`
2. L'application se lancera automatiquement sur `http://127.0.0.1:8000`

### Lancement avec paramètres
1. **Ouvrez un terminal** dans le dossier `dist/`
2. **Lancez avec des commandes Django** :
   ```bash
   # Serveur de développement
   PaintShop.exe runserver
   
   # Serveur sur un port spécifique
   PaintShop.exe runserver 8080
   
   # Autres commandes Django
   PaintShop.exe migrate
   PaintShop.exe createsuperuser
   PaintShop.exe collectstatic
   ```

## 🔧 Fonctionnalités incluses

L'exécutable inclut toutes les fonctionnalités de votre application Django :

- ✅ Interface d'administration
- ✅ Gestion des produits
- ✅ Système de panier
- ✅ Gestion des commandes
- ✅ Système d'authentification
- ✅ Génération de PDF
- ✅ Gestion des images
- ✅ Base de données SQLite

## 🐛 Dépannage

### Problème: "Module not found"
- Vérifiez que toutes les dépendances sont installées
- Relancez le script de création

### Problème: "Port already in use"
- Changez le port : `PaintShop.exe runserver 8080`
- Ou arrêtez le processus qui utilise le port 8000

### Problème: "Database error"
- Vérifiez que `db.sqlite3` est présent dans le dossier `dist/`
- Copiez le fichier depuis le dossier racine si nécessaire

## 📝 Notes importantes

- L'exécutable est autonome et ne nécessite pas Python installé sur la machine cible
- La première exécution peut prendre quelques secondes
- Tous les fichiers nécessaires sont inclus dans le dossier `dist/`
- L'application utilise SQLite par défaut pour la portabilité

## 🔄 Mise à jour

Pour mettre à jour l'exécutable après des modifications :

1. Modifiez votre code Django
2. Relancez `build_exe.bat` ou `python build_exe.py`
3. Remplacez l'ancien exécutable par le nouveau

## 📞 Support

En cas de problème, vérifiez :
1. Les logs dans le terminal
2. La présence de tous les fichiers dans `dist/`
3. Les permissions d'accès au dossier 