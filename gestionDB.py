import sqlite3

connexion = ""
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
        print("Connexion reussie")
    except sqlite3.Error as error:
        print("Erreur de connexion", error)
        
def fermetureDB():
    if connexion:
        connexion.close()
        print("Fermeture DB")
    else:
        print("Erreur de connexion")
        
def verifierExisteTable(table):
    existe = False
    cur = connexion.cursor
    
    sql_tableExiste = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + table + "'"
    
    try:
        cur.execute(sql_tableExiste)
        
        if cur.fetchone()[0]==1:
            existe = True
        else:
            existe = False
    except sqlite3.Error as error:
        print("Erreur verification DB", error)
    
    return existe
        
def creationTable():
    tableMesure = "CREATE TABLE " + table_mesure + " ( " \
        + cle_no + " INTEGER PRIMARY KEY UNIQUE, " \
        + cle_date + " TEXT, " \
        + cle_event + " TEXT, " \
        + cle_val + " TEXT);"
        
    connexionDB
    
    if verifierExisteTable(table_mesure):
        print("Table existe")
    else:
        try:
            connexion.execute(tableMesure)
            print("Creation table")
        except sqlite3 as error:
            print("Erreur lors creation",error)
            
    fermetureDB
    
def ajouterMesure(dateHeureEvenement, typeEvenement, valeurEvenement):
    sql_insert  = "INSERT INTO " + table_mesure + " (" + cle_date + ", " + cle_event + ", " + cle_val + ") VALUES (?,?,?);"
    
    try:
        cur_insert = connexion.cursor()
        donnees_param = (dateHeureEvenement, typeEvenement, valeurEvenement)
        cur_insert.execute(sql_insert, donnees_param)
        connexion.commit()
        print("Enregistrement ajoute dans table")
        cur_insert.close()
    except sqlite3.Error as error:
        print("Erreur enregistrement", error)