import pandas as pd
import sqlite3

# Chemin vers votre fichier CSV
csv_file_path = 'power_consumption_data.csv'

# Lire les données depuis le fichier CSV
data = pd.read_csv(csv_file_path)

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
db_connection = sqlite3.connect('base_de_donnees.db')

# Création d'une table si elle n'existe pas (à adapter selon vos besoins)
db_connection.execute('''
CREATE TABLE IF NOT EXISTS power_data (
    Date TEXT,
    Time TEXT,
    Global_active_power REAL,
    Global_reactive_power REAL,
    Voltage REAL,
    Global_intensity REAL,
    Sub_metering_1 REAL,
    Sub_metering_2 REAL,
    Sub_metering_3 REAL
)
''')

# Insertion des données dans la base de données
data.to_sql('power_data', db_connection, if_exists='append', index=False)

# Fermeture de la connexion à la base de données
db_connection.close()

print("Les données ont été insérées avec succès dans la base de données.")
