# Projet d'Analyse de Données de Vente

Ce projet est une analyse approfondie des données de vente réalisée en **Python 3.10** avec **PyCharm**. L'objectif principal est de manipuler, analyser et visualiser les données de vente afin d'obtenir des **insights exploitables** qui peuvent aider à prendre de meilleures décisions commerciales.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

```sh
pip install pandas matplotlib seaborn
```

- **pandas** : pour la manipulation et l'analyse des données.
- **matplotlib** : pour les visualisations de base.
- **seaborn** : pour des graphiques plus avancés et esthétiques.

## Organisation du Projet

Le projet est structuré en plusieurs dossiers afin de faciliter la gestion des fichiers :

- **data/** : contient les fichiers CSV avec les données de vente.
- **scripts/** : contient les scripts Python pour l'analyse des données.
- **visualisations/** : stocke les graphiques générés par les analyses.

## Chargement et Exploration des Données

Les données sont chargées à l'aide de la bibliothèque **pandas** et nettoyées avant toute analyse. Quelques opérations effectuées :

- **Vérification des valeurs manquantes**
- **Conversion des types de données**
- **Génération de statistiques descriptives**


## 📊 Analyse des Données de Vente  

## 📝 Description du Projet  
Ce projet a pour objectif d'analyser un jeu de données de ventes afin d'identifier des tendances, les produits les plus populaires et les périodes de forte demande. Il est réalisé en équipe dans le cadre de notre cours.  

## 🔍 Mon Rôle dans le Projet  
En tant que membre de l'équipe, ma principale mission était :  
1. **Création d'un jeu de données** :  
   - J'ai généré un fichier CSV contenant des ventes fictives d'une entreprise imaginaire.  
   - Le fichier comprend des colonnes telles que : Produit, Quantité, Revenu, Date de Vente, etc.  
   - Ce jeu de données sert de base pour notre analyse.  

2. **Contribution à l'analyse des ventes** :  
   - J'ai assisté mon collaborateur chargé de l'analyse des ventes dans sa réalisation en Python.  
   - Nous avons utilisé des bibliothèques comme pandas pour explorer et organiser les données.  

## 🗂 Fichiers Importants  
- **sales_fictional_large.csv** : Jeu de données fictif généré pour l'analyse.  
- **analyse_ventes.py** : Script Python utilisé pour analyser les données.  
- **produits_vendus.csv, revenus_par_produit.csv, quantite_par_mois.csv** : Fichiers contenant les résultats de l'analyse.  

## 🛠 Technologies Utilisées  
- **Python (Pandas, NumPy)**  
- **Git & GitHub pour le suivi des versions**  

## 📌 Étapes Suivantes  
🔹 Visualisation des données avec Matplotlib et Seaborn (réalisée par un autre membre de l'équipe).  
🔹 Interprétation des résultats pour formuler des recommandations stratégiques.  
## Visualisation des Données

Pour représenter les données de manière claire et compréhensible, plusieurs types de graphiques sont utilisés en fonction des informations à analyser.

### 1. Produits les plus vendus (Quantité)
   - **Type de graphique** : Diagramme à barres horizontales.
   - **Pourquoi ?** Ce graphique permet de comparer efficacement les quantités vendues des produits et facilite la lecture lorsque les noms des produits sont longs.

### 2. Chiffre d'affaires par produit (Top 10)
   - **Type de graphique** : Diagramme à barres horizontales.
   - **Pourquoi ?** Il permet une comparaison claire des chiffres d'affaires des produits les plus performants.

### 3. Chiffre d'affaires par catégorie
   - **Type de graphique** : Diagramme circulaire (Pie Chart).
   - **Pourquoi ?** Ce graphique est idéal pour visualiser la répartition du chiffre d'affaires entre les catégories de produits.

### 4. Chiffre d'affaires par région
   - **Type de graphique** : Diagramme à barres verticales.
   - **Pourquoi ?** Il permet une comparaison efficace des performances des régions.

### 5. Quantité vendue par mode de paiement
   - **Type de graphique** : Diagramme à barres verticales.
   - **Pourquoi ?** Utile pour analyser le volume des transactions selon les différents modes de paiement.

Toutes les visualisations sont générées avec **Matplotlib** et **Seaborn** pour garantir une présentation claire et lisible des données.

---

### 📢 Remarque  
Ce projet est réalisé uniquement dans un cadre pédagogique et les données utilisées sont entièrement fictives.  

## Auteurs

**ADIGBONON Yoann**
**AGBODJOGBE Merveille**
**WINSOU Astrid**
**DRAMANN Hamzath**

## Licence

Ce projet est sous licence [MIT](LICENSE).

