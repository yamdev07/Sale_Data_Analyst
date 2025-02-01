import matplotlib.pyplot as plt
import seaborn as sns

produits = ["Four", "Machine à laver", "Réfrigérateur", "Canapé", "Smartphone",
            "Chaise", "Ordinateur", "Télévision", "Lit", "Tablette"]
chiffre_affaires = [154894937, 147744771, 145459008, 142395119, 137849672,
                    133876259, 130538013, 123807231, 116387357, 85600907]

plt.figure(figsize=(12, 6))
sns.barplot(x=chiffre_affaires, y=produits, palette="viridis") 

plt.xlabel("Chiffre d'affaires (€)")
plt.ylabel("Produit")
plt.title("Top 10 des produits par chiffre d'affaires")
plt.xticks(rotation=30) 

plt.show()
