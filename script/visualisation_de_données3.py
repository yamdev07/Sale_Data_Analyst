import matplotlib.pyplot as plt
import seaborn as sns

categories = ["Maison", "Électroménager", "Électronique"]
chiffre_affaires = [411432519, 363123919, 543996836]

plt.figure(figsize=(7, 7))
plt.pie(chiffre_affaires, labels=categories, autopct="%1.1f%%", colors=["skyblue", "orange", "lightgreen"])

plt.title("Répartition du chiffre d'affaires par catégorie")

plt.show()

