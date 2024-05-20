import sqlite3

nomDB = "mesure.db"
table_mesure = "resultats"
cle_no = "id"
cle_date = "date"
cle_event = "event"
cle_val = "valEvent"

def connexionDB():
    global connexion
    try:
        connexion = sqlite3.connect(nomDB)
        print("Connexion réussie")
        return connexion
    except sqlite3.Error as error:
        print("Erreur de connexion", error)
        return None

def fermetureDB(connexion):
    if connexion:
        connexion.close()
        print("Fermeture DB")
    else:
        print("Erreur de connexion")

def creationTable(connexion):
    tableMesure = f"CREATE TABLE IF NOT EXISTS {table_mesure} (" \
                   f"{cle_no} INTEGER PRIMARY KEY UNIQUE, " \
                   f"{cle_date} TEXT, " \
                   f"{cle_event} TEXT, " \
                   f"{cle_val} TEXT);"
    try:
        connexion.execute(tableMesure)
        print("Création table")
    except sqlite3.Error as error:
        print("Erreur lors de la création", error)

def ajouterMesure(dateHeureEvenement, typeEvenement, valeurEvenement):
    sql_insert = f"INSERT INTO {table_mesure} ({cle_date}, {cle_event}, {cle_val}) VALUES (?,?,?);"

    try:
        cur_insert = connexion.cursor()
        donnees_param = (dateHeureEvenement, typeEvenement, valeurEvenement)
        cur_insert.execute(sql_insert, donnees_param)
        connexion.commit()
        print("Enregistrement ajouté dans table")
        cur_insert.close()
    except sqlite3.Error as error:
        print("Erreur enregistrement", error)

