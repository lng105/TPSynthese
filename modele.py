import json, datetime

class Modele:
    def __init__(self, valeurEvenement):
        self.dateHeureEvenement = datetime.datetime.now()
        self.typeEvenement = {"Activation du systeme d'alarme", "Deactivation du systeme d'alarme", "Acces valide du systeme d'alarme", "Acces invalide du systeme d'alarme"}
        self.valeurEvenement = valeurEvenement
        
    @property
    def dateHeureEvenement(self):
        return self._dateHeureEvenement
    
    @dateHeureEvenement.setter
    def dateHeureEvenement(self, value):
        self._dateHeureEvenement = value
    
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
