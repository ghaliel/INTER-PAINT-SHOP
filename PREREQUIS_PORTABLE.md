# 🎨 PaintShop - Prérequis pour l'Exécutable Portable

## ✅ Prérequis Système

### Système d'exploitation
- **Windows 10** (version 1903 ou plus récente)
- **Windows 11** (toutes versions)
- **Windows Server 2019/2022** (pour usage serveur)

### Architecture
- **x64 (64-bit)** - Recommandé
- **x86 (32-bit)** - Compatible mais non testé

### Espace disque
- **Minimum** : 200 MB d'espace libre
- **Recommandé** : 500 MB d'espace libre
- **Pour les données** : 1 GB supplémentaire selon l'usage

### Mémoire RAM
- **Minimum** : 4 GB RAM
- **Recommandé** : 8 GB RAM ou plus
- **Pour de gros volumes** : 16 GB RAM

## 🔧 Prérequis Logiciels

### Aucune installation requise !
L'exécutable portable **ne nécessite AUCUNE installation** de :
- ❌ Python
- ❌ Django
- ❌ Base de données
- ❌ Serveur web
- ❌ Dépendances

### Navigateur web
- **Chrome** 90+ (recommandé)
- **Firefox** 88+
- **Edge** 90+
- **Safari** 14+ (si compatible Windows)

## 🚀 Installation et Lancement

### Étape 1 : Copie des fichiers
1. **Copiez** tout le contenu du dossier `dist_portable/`
2. **Collez** dans un dossier sur le PC cible
3. **Vérifiez** que tous les fichiers sont présents :
   - `PaintShop_Portable.exe`
   - `Lancer_PaintShop.bat`
   - `README.txt`
   - `db.sqlite3`
   - Dossiers `static/`, `media/`, etc.

### Étape 2 : Lancement
1. **Double-cliquez** sur `PaintShop_Portable.exe`
2. **Ou** double-cliquez sur `Lancer_PaintShop.bat`
3. **Attendez** le démarrage (10-30 secondes)
4. **Ouvrez** votre navigateur sur `http://127.0.0.1:8000`

## 🛡️ Sécurité et Permissions

### Permissions requises
- **Lecture/Écriture** sur le dossier de l'application
- **Accès réseau** pour le serveur local (port 8000)
- **Exécution** de fichiers .exe

### Antivirus
- **Autorisez** l'exécutable dans votre antivirus
- **Ajoutez** le dossier à la liste blanche si nécessaire
- **Désactivez temporairement** l'antivirus si problème

### Pare-feu Windows
- **Autorisez** l'application dans le pare-feu Windows
- **Port 8000** doit être accessible localement

## 🐛 Dépannage des Prérequis

### Problème : "Application ne peut pas démarrer"
**Solutions :**
1. Vérifiez que Windows est à jour
2. Installez les Visual C++ Redistributables :
   - [Microsoft Visual C++ Redistributable 2015-2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)
3. Vérifiez les permissions d'exécution

### Problème : "Port déjà utilisé"
**Solutions :**
1. Changez le port : `PaintShop_Portable.exe runserver 8080`
2. Fermez les applications qui utilisent le port 8000
3. Redémarrez le PC si nécessaire

### Problème : "Accès refusé"
**Solutions :**
1. Exécutez en tant qu'administrateur
2. Vérifiez les permissions du dossier
3. Désactivez temporairement l'antivirus

### Problème : "Fichiers manquants"
**Solutions :**
1. Recopiez tous les fichiers du dossier `dist_portable/`
2. Vérifiez l'intégrité des fichiers
3. Téléchargez à nouveau l'exécutable

## 📋 Checklist de Vérification

### Avant le lancement
- [ ] Windows 10/11 installé
- [ ] 4 GB RAM minimum
- [ ] 200 MB espace disque libre
- [ ] Tous les fichiers copiés
- [ ] Antivirus configuré
- [ ] Pare-feu configuré

### Après le lancement
- [ ] Application démarre sans erreur
- [ ] Interface web accessible
- [ ] Base de données fonctionnelle
- [ ] Images et fichiers statiques chargés
- [ ] Toutes les fonctionnalités opérationnelles

## 🔄 Mise à jour

### Pour mettre à jour l'application
1. **Arrêtez** l'application en cours
2. **Remplacez** tous les fichiers par les nouveaux
3. **Conservez** `db.sqlite3` si vous voulez garder les données
4. **Relancez** l'application

## 📞 Support

### En cas de problème
1. **Vérifiez** les prérequis ci-dessus
2. **Consultez** le fichier `README.txt`
3. **Testez** sur un autre PC
4. **Contactez** le support technique

## 🎯 Résumé

**Prérequis minimaux :**
- Windows 10/11 (64-bit)
- 4 GB RAM
- 200 MB espace disque
- Navigateur web moderne
- Permissions d'exécution

**Aucune installation requise !** L'exécutable portable contient tout ce qui est nécessaire pour fonctionner.

---

**🎨 PaintShop - Prêt à l'emploi sur n'importe quel PC Windows !** 