# Frontend - Projet APA

Interface utilisateur du tableau de bord d'analyse d'Achat, développée avec Vue 3 et Vite.

## 🚀 Fonctionnalités

- 📊 Tableau de bord interactif
- 💰 Suivi des ventes totales
- 📈 Visualisation des produits les plus vendus
- 🔄 Analyse par période (7 jours, 30 jours, 12 mois)
- 📱 Interface responsive
- 🎨 Design moderne avec TailwindCSS
- 📊 Graphiques interactifs avec Chart.js

## 🛠️ Prérequis

- Node.js 
- npm
- Backend API en cours d'exécution

## ⚙️ Installation

1. Clonez le repository :
```bash
git clone <repository-url>
cd FrontEnd
```

2. Installez les dépendances :
```bash
npm install
```

## 🚀 Démarrage

### Mode développement
```bash
npm run dev
```
L'application sera accessible sur `http://localhost:5173`

### Construction pour la production
```bash
npm run build
```

### Lancer les tests
```bash
npm run test
```

## 📁 Structure du projet

```
FrontEnd/
├── src/
│   ├── components/     # Composants réutilisables
│   │   ├── StatisticsCards.vue    # Cartes de statistiques
│   │   └── ChartSection.vue       # Section des graphiques
│   ├── assets/        # Images et styles
│   └── App.vue        # Composant principal
├── public/           # Fichiers statiques
└── index.html       # Point d'entrée HTML
```

## 📊 Composants principaux

### StatisticsCards
- Affiche les statistiques clés
- Total des ventes
- Top 3 des produits les plus vendus
- Répartition des ventes par catégorie

### ChartSection
- Graphique en secteurs pour les catégories
- Graphique en barres pour les ventes de produits

## 🔄 Gestion des périodes

L'application permet d'analyser les données sur différentes périodes :
- 7 derniers jours (7d)
- 30 derniers jours (30d)
- 12 derniers mois (12m)

## 🎨 Personnalisation

L'interface utilise TailwindCSS pour le style. Vous pouvez personnaliser :
- Les couleurs dans `tailwind.config.js`
- Les composants dans `/src/components`


## 📱 Responsive Design

L'interface s'adapte automatiquement à différentes tailles d'écran :
- Mobile 
- Tablette 
- Desktop 

## ⚠️ Dépannage

1. Si l'API n'est pas accessible :
   - Vérifiez que le backend est en cours d'exécution
   - Vérifiez l'URL dans le fichier `.env`
   - Vérifiez les logs dans la console du navigateur

2. Si les graphiques et les données ne s'affichent pas :
   - attendez le chargement des données
   - Vérifiez que les données sont bien reçues de l'API
   - Consultez la console pour les erreurs éventuelles


