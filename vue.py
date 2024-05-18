import tkinter as tk
from tkinter import ttk

class Vue(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.btn_debuterSyst=ttk.Button(self, text="Start System", command=self.btn_start)
        self.btn_debuterSyst.pack()
        
        self.btn_arreterSyst=ttk.Button(self, text="Stop System", command=self.btn_stop)
        self.btn_arreterSyst.pack(pady=10)
        
        self.btn_valider=tk.Button(self, text="Valider", state="disabled",command=self.btn_valider) 
        self.btn_valider.pack()
        
        self.journal_desc=tk.Label(self, text= "Journal d'events")
        self.journal_desc.pack()
        
        self.journal_listbox = tk.Listbox(self, height=10, width=45)
        self.journal_listbox.pack(pady=5)
        
        self.btn_sauvegarder=tk.Button(self, text="Sauvegarder en JSON")
        self.btn_sauvegarder.pack()
        
        self.label_actif=tk.Label(self, text= "Systeme desactive")
        self.label_actif.pack()
        
        self.controleur = None
        
    def set_controleur(self, p_controleur):
        self.controleur = p_controleur
        
    def disable_valider_button(self):
        self.btn_valider.config(state="disabled")
        
    def btn_start(self):
        self.controleur.start_system()
        self.label_actif.config(text="Système activé", fg="green")
        self.btn_valider.config(state=tk.NORMAL)
        
    def btn_stop(self):    
        self.controleur.stop_system()
        self.label_actif.config(text="Système desactivé", fg="red")
        self.btn_valider.config(state="disabled")
        
    def btn_valider(self):
        self.controleur.validate_code()