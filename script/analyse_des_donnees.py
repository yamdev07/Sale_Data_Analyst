import pandas as pd
 

# Charger les données depuis le fichier CSV
csv_file_path = "C:\python_projet\Sale_Data_Analyst\data\sales_fictional_large.csv" 
sales_data = pd.read_csv(csv_file_path)

# Convertir "Date de Vente" en type datetime pour les analyses de date
sales_data["Date de Vente"] = pd.to_datetime(sales_data["Date de Vente"], errors='coerce')

# 1. Produits les plus vendus en termes de quantité
top_products = sales_data.groupby("Produit")["Quantité"].sum().sort_values(ascending=False).head(10)

# 2. Analyse des revenus (chiffre d'affaires par produit, catégorie et région)
revenue_by_product = sales_data.groupby("Produit")["Chiffre d'Affaires"].sum().sort_values(ascending=False).head(10)
revenue_by_category = sales_data.groupby("Catégorie")["Chiffre d'Affaires"].sum()
revenue_by_region = sales_data.groupby("Région")["Chiffre d'Affaires"].sum()

# 3. Quantité vendue par mode de paiement
quantity_by_payment = sales_data.groupby("Mode de Paiement")["Quantité"].sum()

# 4. Identifier la date avec les ventes les plus élevées
sales_by_date = sales_data.groupby("Date de Vente")["Chiffre d'Affaires"].sum()
top_sales_date = sales_by_date.idxmax(), sales_by_date.max()

# Affichage des résultats
print("1. Produits les plus vendus (Quantité) :")
print(top_products)

print("\n2. Chiffre d'affaires par produit (Top 10) :")
print(revenue_by_product)

print("\n3. Chiffre d'affaires par catégorie :")
print(revenue_by_category)

print("\n4. Chiffre d'affaires par région :")
print(revenue_by_region)

print("\n5. Quantité vendue par mode de paiement :")
print(quantity_by_payment)

print("\n6. Date avec les ventes les plus élevées :")
print(f"Date : {top_sales_date[0]}, Chiffre d'affaires : {top_sales_date[1]:,.2f} FCFA")
