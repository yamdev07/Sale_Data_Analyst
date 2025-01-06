if __name__ == '__main__':
    import os
    import pandas as pd

    # Créer un DataFrame fictif
    data = {
        'Produit': ["Ordinateur", "Smartphone", "Tablette", "Clavier", "Souris", "Woofer", "Ring-light"],
        'Quantité': [10, 20, 15, 30, 25, 30, 22],
        'Prix Unitaire': [10000, 7000, 9000, 4000, 2500, 4500, 8000],
    }

    df = pd.DataFrame(data)

    # Vérifier si le dossier 'data' existe, sinon le créer
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Sauvegarder dans le dossier 'data'
    csv_file_path = os.path.join(data_folder, 'sales.csv')
    df.to_csv(csv_file_path, index=False)

    print(f"Le fichier CSV a été généré à l'emplacement : {csv_file_path}")
