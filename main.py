import vue as v
import modele as m
import controlleur as c
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Programme Synthese")
        
        vue = v.Vue(self)
        vue.grid(row=0,column=0,padx=50,pady=50)
        
if __name__ == '__main__':
    app = App()
    app.mainloop()