import matplotlib.pyplot as plt
import seaborn as sns

regions = ["Centre", "Est", "Nord", "Ouest", "Sud"]
chiffre_affaires = [253681648, 288004126, 256720899, 262840786, 257305815]

plt.figure(figsize=(8, 5))
sns.barplot(x=regions, y=chiffre_affaires, palette="coolwarm")

plt.xlabel("Région")
plt.ylabel("Chiffre d'affaires (€)")
plt.title("Chiffre d'affaires par région")

plt.show()
