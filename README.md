
Ce code effectue deux tâches principales : la création d'un fichier CSV contenant des informations sur les fichiers trouvés dans un répertoire spécifié et l'insertion de ces informations dans une base de données PostgreSQL.

## 1. Création du fichier CSV
Importation des modules nécessaires : os pour interagir avec le système de fichiers, csv pour manipuler les fichiers CSV et psycopg2 pour interagir avec PostgreSQL.

#### Définition des chemins :

Le répertoire à scanner pour les fichiers.
```console
directory_to_search
```


Le fichier CSV où les informations seront sauvegardées :
```console
output_csv_file 
```


#### Ouverture et écriture dans le fichier CSV :

Ouvre le fichier CSV en mode écriture avec un encodage UTF-8.
```console
"w"
```

Initialise un objet écrivain CSV 
```console
writer_csv
```

Écrit l'en-tête du fichier CSV :
```console
 ["nom_fichier", "emplacement", "poids_bytes"]
```


#### Parcours du répertoire :

Pour parcourir récursivement le répertoire spécifié, on utilise :
```console
os.walk
```

Pour chaque fichier trouvé, obtient le chemin complet et la taille du fichier.

Écrit les informations du fichier (nom, chemin, taille) dans le CSV.

Affiche un message d'avertissement si la taille du fichier dépasse 1000 octets.

#### Fermeture du fichier CSV :

Ferme le fichier CSV après avoir terminé l'écriture, ce qui est crucial pour s'assurer que les données sont bien sauvegardées.

## 2. Insertion des données dans PostgreSQL

### Paramètres de connexion :
Définit les paramètres de connexion pour la base de données PostgreSQL.
```console
conn_params
```

### Connexion à la base de données :
Pour se connecter à la base de données avec les paramètres fournis, on utilise : 
```console
psycopg2.connect
```


Initialise un curseur pour exécuter les requêtes :
```console
cur
```

### Lecture et insertion des données du fichier CSV :
Ouvre le fichier CSV en mode lecture :
```console
"r"
```


### Lit les en-têtes du CSV pour créer une requête d'insertion dynamique.

Parcourt chaque ligne du fichier CSV et exécute la requête d'insertion correspondante dans la table PostgreSQL spécifiée :
```console
schema_name.table_name
```


### Validation et fermeture de la connexion :

Valide les transactions avec 
```console
conn.commit
```


Ferme le curseur et la connexion à la base de données.

### Message de fin :
Affiche un message indiquant que l'insertion des données est terminée.
