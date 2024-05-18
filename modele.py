import json, datetime

class Modele:
    def __init__(self, p_typeEvenement, p_valeurEvenement):
        self.dateHeureEvenement = datetime.datetime.now()
        self.typeEvenement = p_typeEvenement
        self.valeurEvenement = p_valeurEvenement

    @property
    def typeEvenement(self):
        return self._typeEvenement
    
    @typeEvenement.setter
    def typeEvenement(self, value):
        self._typeEvenement = value
    
    @property
    def valeurEvenement(self):
        return self._valeurEvenement
    
    @valeurEvenement.setter
    def valeurEvenement(self, value):
        self._valeurEvenement = value
    
    def __repr__(self):
        return f"{self.dateHeureEvenement} - {self.valeurEvenement}"

    def afficherMesure(self):
        print("Date:" + {self.dateHeureEvenement})
        print("Type:" + {self.typeEvenement})
        print("Valeur:" + {self.valeurEvenement})

    def saveFichier(self):
        try:
            with open("resultats.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {"resultats": []}
            
        data["resultats"].append({
            "dateHeureEvenement": self.dateHeureEvenement.strftime("%Y-%m-%d %H:%M:%S"),
            "typeEvenement": self.typeEvenement,
        })
        with open("resultats.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
