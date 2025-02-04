
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
L'analyse des données de vente a été réalisée en plusieurs étapes clés :

 1. ## Préparation et Chargement des Données

Les données ont été générées sous forme de fichiers CSV, comprenant des informations sur les produits, les quantités, les revenus, et les dates de vente.
Le fichier sales_fictional_large.csv a été chargé dans un DataFrame à l'aide de pandas.
Une première étape de nettoyage a permis de vérifier les valeurs manquantes, les doublons, et d'ajuster les types de données.
## 2. 🔍 Exploration Initiale des Données

Une fois les données nettoyées, des statistiques descriptives ont été générées pour mieux comprendre les tendances de base à l'aide des fonctions df.describe() et df.info().
 ## 3. 📝Analyse des Tendances de Vente

Des analyses ont été effectuées pour identifier les produits les plus vendus, les produits générant le plus de revenus et les périodes de forte demande.
Les données ont été regroupées par produit, par région et par mode de paiement pour comprendre les comportements d'achat.
## 4. Calcul des KPIs

Des indicateurs clés de performance (KPIs) ont été calculés pour évaluer la performance de chaque produit, comme le revenu total par produit, la quantité totale vendue par mois, et le chiffre d'affaires par région.  

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


![ Quantité vendue par mode de paiement](https://github.com/user-attachments/assets/2bf18a4a-28b9-421b-8a86-7a9f681fe357)
![Chiffre d'affaires par région](https://github.com/user-attachments/assets/22c93a67-1011-427d-92d3-e8638aa6aa69)
![Chiffre d'affaires par catégorie](https://github.com/user-attachments/assets/a63e81f8-6c8a-4566-96e9-7002fd834194)
![Chiffre d'affaires par produit](https://github.com/user-attachments/assets/5f531158-348e-458c-a9b7-5c8535af420b)
![Produits les plus vendus](https://github.com/user-attachments/assets/d79965f5-c628-43a1-a2c2-9b6d4dfe5222)

Toutes les visualisations sont générées avec **Matplotlib** et **Seaborn** pour garantir une présentation claire et lisible des données.

---

### 📢 Remarque  
Ce projet est réalisé uniquement dans un cadre pédagogique et les données utilisées sont entièrement fictives.  

## Auteurs

**ADIGBONON Yoann**
**AGBODJOGBE Merveille**
**WINSOU Astrid**
**DRAMANE Hamzath**

## Licence

Ce projet est sous licence [MIT](LICENSE).

