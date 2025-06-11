# 🎨 INTER PAINT - Déploiement avec www.InterPaint.ma

## 🚀 Déploiement sur Railway

### **Étape 1: Déployer sur Railway**

1. **Allez sur [railway.app](https://railway.app)**
2. **Connectez-vous avec GitHub**
3. **Créez un nouveau projet** → "Deploy from GitHub repo"
4. **Sélectionnez** `ghaliel/INTER-PAINT-SHOP`
5. **Attendez que le déploiement se termine**

### **Étape 2: Configurer les variables d'environnement**

Dans Railway, allez dans "Variables" et ajoutez :

```
SECRET_KEY=django-insecure-production-key-change-this-to-something-secure
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app,www.interpaint.ma,interpaint.ma
```

### **Étape 3: Obtenir l'URL Railway**

Votre site sera accessible à : `https://your-app-name.railway.app`

## 🌐 Configuration du domaine www.InterPaint.ma

### **Étape 1: Acheter le domaine**

1. **Allez sur [iam.ma](https://iam.ma)** ou [anrt.ma](https://anrt.ma)
2. **Recherchez** `InterPaint.ma`
3. **Achetez le domaine** (200-500 MAD/an)

### **Étape 2: Configurer les DNS**

Dans votre panneau de gestion de domaine, configurez les DNS :

#### **Pour Railway :**
```
Type: CNAME
Nom: www
Valeur: your-app-name.railway.app
TTL: 3600

Type: A
Nom: @
Valeur: 76.76.19.19
TTL: 3600
```

#### **Alternative - Redirection :**
```
Type: CNAME
Nom: @
Valeur: your-app-name.railway.app
TTL: 3600

Type: CNAME
Nom: www
Valeur: your-app-name.railway.app
TTL: 3600
```

### **Étape 3: Configurer Railway pour le domaine personnalisé**

1. **Dans Railway**, allez dans votre projet
2. **Cliquez sur "Settings"**
3. **Trouvez "Custom Domains"**
4. **Ajoutez** :
   - `www.interpaint.ma`
   - `interpaint.ma`

### **Étape 4: Mettre à jour ALLOWED_HOSTS**

Modifiez les variables d'environnement dans Railway :

```
ALLOWED_HOSTS=your-app-name.railway.app,www.interpaint.ma,interpaint.ma
```

## 🔧 Configuration SSL/HTTPS

### **Railway (Automatique)**
- Railway configure automatiquement SSL
- Votre site sera accessible en HTTPS

### **Vérification**
- `https://www.interpaint.ma` ✅
- `https://interpaint.ma` ✅ (redirige vers www)

## 📧 Configuration Email (Optionnel)

Pour les emails professionnels, configurez :

### **Google Workspace**
1. Allez sur [workspace.google.com](https://workspace.google.com)
2. Choisissez le plan "Business Starter" (60 MAD/mois)
3. Configurez les MX records dans votre DNS

### **MX Records pour Google Workspace :**
```
Type: MX
Priorité: 1
Valeur: aspmx.l.google.com

Type: MX
Priorité: 5
Valeur: alt1.aspmx.l.google.com

Type: MX
Priorité: 5
Valeur: alt2.aspmx.l.google.com
```

## 🎯 Résultat Final

Votre site sera accessible à :
- **Site principal** : `https://www.interpaint.ma`
- **Sans www** : `https://interpaint.ma` (redirige vers www)
- **Email** : `contact@interpaint.ma`

## ⚠️ Important

1. **Attendez 24-48h** pour la propagation DNS
2. **Testez** : `ping www.interpaint.ma`
3. **Vérifiez SSL** : Le cadenas vert dans le navigateur
4. **Sauvegardez** vos informations de domaine

## 🆘 Support

- **ANRT** : [anrt.ma](https://anrt.ma) - Support technique
- **Railway** : [railway.app](https://railway.app) - Support déploiement
- **Google Workspace** : Support 24/7 pour email 