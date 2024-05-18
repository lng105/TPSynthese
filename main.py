import vue as v
import modele as m
import controleur as c
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Programme Synthese")
        
        modele = m.Modele("","")
        
        vue = v.Vue(self)
        vue.grid(row=0,column=0,padx=75,pady=75)
        
        controleur = c.Controleur(modele, vue)
        
        vue.set_controleur(controleur)
        
if __name__ == '__main__':
    app = App()
    app.mainloop()