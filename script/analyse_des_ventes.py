if __name__ == '__main__':
    import os
    import pandas as pd

    # Chemin du fichier CSV
    csv_file = 'C:/Users/yoannyamd/PycharmProjects/Sale_Data_Analyst/data/sales.csv'


    # Vérifier si le fichier existe
    if not os.path.exists(csv_file):
        print(f"Le fichier {csv_file} est introuvable.")
    else:
        # Charger les données
        df = pd.read_csv(csv_file)

        # Afficher un aperçu
        print("Aperçu des données :")
        print(df.head())
