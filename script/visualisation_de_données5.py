import matplotlib.pyplot as plt
import seaborn as sns

modes_de_paiement = ["Carte bancaire", "Espèces", "Mobile Money"]
quantites = [8171, 8657, 8829]

plt.figure(figsize=(8, 5))
sns.barplot(x=modes_de_paiement, y=quantites, palette="pastel")

plt.xlabel("Mode de paiement")
plt.ylabel("Quantité vendue")
plt.title("Quantité vendue par mode de paiement")

plt.show()
