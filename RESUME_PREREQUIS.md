# 🎨 PaintShop - Prérequis pour l'Exécutable Portable

## ✅ Prérequis Minimaux

### Système d'exploitation
- **Windows 10** (version 1903+) ou **Windows 11**
- **Architecture x64** (64-bit) recommandée

### Ressources matérielles
- **RAM** : 4 GB minimum (8 GB recommandé)
- **Espace disque** : 200 MB minimum (500 MB recommandé)
- **Processeur** : Compatible x64

### Logiciels
- **Navigateur web** : Chrome 90+, Firefox 88+, Edge 90+
- **Aucune installation** de Python, Django ou base de données requise

## 🚀 Installation et Lancement

### Étape 1 : Copie
1. **Copiez** tout le contenu du dossier `dist_portable/`
2. **Collez** dans un dossier sur le PC cible
3. **Vérifiez** que tous les fichiers sont présents

### Étape 2 : Lancement
1. **Double-cliquez** sur `PaintShop_Portable.exe`
2. **Attendez** le démarrage (10-30 secondes)
3. **Ouvrez** votre navigateur sur `http://127.0.0.1:8000`

## 🛡️ Configuration Sécurité

### Permissions requises
- **Lecture/Écriture** sur le dossier de l'application
- **Accès réseau** pour le serveur local (port 8000)
- **Exécution** de fichiers .exe

### Antivirus et Pare-feu
- **Autorisez** l'exécutable dans votre antivirus
- **Ajoutez** le dossier à la liste blanche si nécessaire
- **Autorisez** l'application dans le pare-feu Windows

## 🐛 Dépannage Rapide

### Problème : Application ne démarre pas
1. Vérifiez Windows 10/11
2. Installez [Visual C++ Redistributables](https://aka.ms/vs/17/release/vc_redist.x64.exe)
3. Désactivez temporairement l'antivirus

### Problème : Port déjà utilisé
```bash
PaintShop_Portable.exe runserver 8080
# Puis ouvrez: http://127.0.0.1:8080
```

### Problème : Fichiers manquants
1. Recopiez le dossier `dist_portable/` complet
2. Vérifiez l'intégrité des fichiers

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
- [ ] Toutes les fonctionnalités opérationnelles

## 🎯 Résumé

**Prérequis essentiels :**
- Windows 10/11 (64-bit)
- 4 GB RAM
- 200 MB espace disque
- Navigateur web moderne
- Permissions d'exécution

**Aucune installation requise !** L'exécutable portable contient tout ce qui est nécessaire pour fonctionner.

---

**🎨 PaintShop - Prêt à l'emploi sur n'importe quel PC Windows !** 