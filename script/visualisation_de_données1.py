import matplotlib.pyplot as plt
import seaborn as sns

produits = ["Réfrigérateur", "Four", "Ordinateur", "Canapé", "Chaise",
            "Machine à laver", "Smartphone", "Télévision", "Lit", "Tablette"]
quantites = [2953, 2927, 2840, 2720, 2707, 2566, 2455, 2339, 2127, 2023]

plt.figure(figsize=(10, 6))
sns.barplot(x=quantites, y=produits, palette="Blues_r")  # Inverser x et y pour un meilleur affichage

plt.xlabel("Quantité vendue")
plt.ylabel("Produit")
plt.title("Top 10 des produits les plus vendus")

plt.show()