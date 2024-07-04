import os
import csv
import psycopg2

# Répertoire à scanner : 
directory_to_search = "C:\\Users\\hsofia\\Desktop\\"

# Fichier d'audit
output_csv_file = 'C:\\Users\\hsofia\\Desktop\\fichier_trouves.csv'

# Ouvrir le fichier csv
csv_file = open(output_csv_file, mode="w", encoding='utf-8', newline='')

#Ecrire dans le fichier csv
writer_csv = csv.writer(csv_file)

# Ecriture de l'entête du CSV 
writer_csv.writerow(["nom_fichier", "emplacement", "poids_bytes"])

#Parcourir les répertoire pour lister les fichiers trouvés
for root, dir, files in os.walk(directory_to_search):
    for file in files:
        #variable 
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(os.path.join(root, file))
        writer_csv.writerow([
            file,
            file_path,
            file_size
            ])
        
        if file_size > 1000:
            print("Attention gros fichier :", file, " - Poids ", os.path.getsize(os.path.join(root, file)))

# Penser à fermer le fichier csv ! Mega important 
csv_file.close()



# Paramètres de connexion à la base de données
conn_params = {
    "host": "localhost",
    "port": 5433,
    "database": "postgres",
    "user": "postgres",
    "password": "postgres"
}


# Nom de la table et du schema dans laquelle insérer les données
schema_name = "test"
table_name = "mon_csv"

# Connexion à la base de données
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

# Lecture du fichier CSV et insertion des données
with open(output_csv_file, 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)  # Lire la première ligne comme en-têtes
    
    # Créer la requête d'insertion
    insert_query = f"INSERT INTO {schema_name}.{table_name} ({','.join(headers)}) VALUES ({','.join(['%s']*len(headers))})"
    
    # Insérer chaque ligne du CSV
    for row in csv_reader:
        cur.execute(insert_query, row)

# Valider les changements et fermer la connexion
conn.commit()
cur.close()
conn.close()

print("Insertion des données terminée.")