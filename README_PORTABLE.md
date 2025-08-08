# 🎨 PaintShop - Exécutable Portable

## 📋 Vue d'ensemble

Ce projet permet de créer un **exécutable portable** de votre application Django PaintShop qui peut être copié et exécuté sur n'importe quel PC Windows sans installation.

## 🚀 Création de l'Exécutable Portable

### Méthode 1: Script batch automatique (Recommandé)

1. **Double-cliquez** sur `build_portable.bat`
2. Attendez que le processus se termine (5-10 minutes)
3. L'exécutable portable sera créé dans le dossier `dist_portable/`

### Méthode 2: Commande manuelle

```bash
# Installer les dépendances
pip install -r requirements.txt

# Créer l'exécutable portable
python build_portable_exe.py
```

## 📁 Structure de l'Exécutable Portable

```
dist_portable/
├── PaintShop_Portable.exe    # Exécutable principal
├── Lancer_PaintShop.bat      # Script de lancement
├── README.txt                # Instructions d'utilisation
├── db.sqlite3               # Base de données
├── static/                  # Fichiers statiques
├── media/                   # Fichiers média
├── templates/               # Templates Django
└── staticfiles/             # Fichiers statiques collectés
```

## 🎯 Utilisation de l'Exécutable Portable

### Distribution

1. **Copiez** tout le contenu du dossier `dist_portable/`
2. **Collez** sur n'importe quel PC Windows
3. **Double-cliquez** sur `PaintShop_Portable.exe`
4. L'application se lance automatiquement sur `http://127.0.0.1:8000`

### Méthodes de lancement

#### Méthode 1: Double-clic simple
- Double-cliquez sur `PaintShop_Portable.exe`
- L'application se lance automatiquement

#### Méthode 2: Script batch
- Double-cliquez sur `Lancer_PaintShop.bat`
- Suivez les instructions à l'écran

#### Méthode 3: Ligne de commande
```bash
# Serveur de développement
PaintShop_Portable.exe runserver

# Serveur sur un port spécifique
PaintShop_Portable.exe runserver 8080

# Autres commandes Django
PaintShop_Portable.exe migrate
PaintShop_Portable.exe createsuperuser
PaintShop_Portable.exe collectstatic
```

## 🔧 Fonctionnalités Incluses

L'exécutable portable inclut **toutes** les fonctionnalités de votre application Django :

- ✅ **Interface d'administration** - Gestion complète du site
- ✅ **Gestion des produits** - Ajout, modification, suppression
- ✅ **Système de panier** - Ajout, modification, suppression d'articles
- ✅ **Gestion des commandes** - Suivi, statuts, historique
- ✅ **Système d'authentification** - Inscription, connexion, profils
- ✅ **Génération de PDF** - Factures, rapports, commandes
- ✅ **Gestion des images** - Upload, redimensionnement, affichage
- ✅ **Base de données SQLite** - Données locales et portables
- ✅ **Interface responsive** - Compatible mobile et desktop

## 🐛 Dépannage

### Problème: Port déjà utilisé
```bash
# Changez le port
PaintShop_Portable.exe runserver 8080
# Puis ouvrez: http://127.0.0.1:8080
```

### Problème: Application ne démarre pas
1. Vérifiez que tous les fichiers sont présents dans le dossier
2. Essayez de lancer via `Lancer_PaintShop.bat`
3. Vérifiez les permissions d'accès au dossier

### Problème: Base de données corrompue
1. Supprimez `db.sqlite3`
2. Relancez l'application
3. Une nouvelle base sera créée automatiquement

### Problème: Fichiers statiques manquants
1. Vérifiez que les dossiers `static/` et `media/` sont présents
2. Relancez l'application
3. Les fichiers seront recréés si nécessaire

## 📝 Notes Importantes

### Avantages de l'exécutable portable

- 🎯 **Aucune installation requise** - Fonctionne immédiatement
- 📁 **Autonome** - Tous les fichiers inclus
- 🔄 **Portable** - Copiable sur n'importe quel PC Windows
- 🛡️ **Sécurisé** - Base de données locale
- ⚡ **Rapide** - Démarrage en quelques secondes

### Limitations

- 🖥️ **Windows uniquement** - Compatible Windows 10/11
- 💾 **Base locale** - Données non synchronisées entre PC
- 🔌 **Hors ligne** - Pas de fonctionnalités en ligne

## 🔄 Mise à Jour

Pour mettre à jour l'exécutable portable :

1. **Modifiez** votre code Django
2. **Relancez** `build_portable.bat`
3. **Remplacez** l'ancien exécutable par le nouveau
4. **Conservez** la base de données si nécessaire

## 🧪 Tests

Pour tester la portabilité :

```bash
# Test de la configuration
python test_portable.py

# Test des commandes Django
PaintShop_Portable.exe check
PaintShop_Portable.exe showmigrations
```

## 📞 Support

En cas de problème :

1. **Vérifiez** les logs dans le terminal
2. **Consultez** le fichier `README.txt` dans le dossier portable
3. **Testez** avec `test_portable.py`
4. **Relancez** l'application

## 🎉 Félicitations !

Votre application Django PaintShop est maintenant **portable** et peut être distribuée facilement sur n'importe quel PC Windows sans modification des fonctionnalités ! 