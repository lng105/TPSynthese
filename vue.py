import tkinter as tk
import json, LCD1602
import tkinter as tk
import RPi.GPIO as GPIO
import KeypadGPIO as c
from tkinter import ttk
from gpiozero import LED, MotionSensor, Buzzer
from time import sleep

LIGNES = 4
COLONNES = 4
lignesGPIO = [21,20,16,12]
colonnesGPIO = [26,19,13,6]

touches = ['1','2','3','A',
           '4','5','6','B',
           '7','8','9','C',
           '*','0','#','D']

buzzer = Buzzer(23)
led_rouge = LED(27)
led_vert = LED(22)
LCD1602.init(0x3f, 1)

class Vue(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.btn_debuterSyst=ttk.Button(self, text="Start System", command=self.start_system)
        self.btn_debuterSyst.pack()
        
        self.btn_arreterSyst=ttk.Button(self, text="Stop System", command=self.stop_system)
        self.btn_arreterSyst.pack(pady=10)
        
        self.btn_valider=tk.Button(self, text="Valider", state="disabled")
        self.btn_valider.pack()
        
        self.journal_desc=tk.Label(self, text= "Journal d'events")
        self.journal_desc.pack()
        
        self.journal_listbox = tk.Listbox(self, height=10, width=30)
        self.journal_listbox.pack(pady=5)
        
        self.btn_sauvegarder=tk.Button(self, text="Sauvegarder en JSON")
        self.btn_sauvegarder.pack()
        
        self.label_actif=tk.Label(self, text= "Systeme desactive")
        self.label_actif.pack()
        
    def start_system(self):
        led_rouge.off()
        led_vert.on()
        self.label_actif.config(text="Système activé", fg="green")
        self.btn_valider.config(state=tk.NORMAL)
        
    def stop_system(self):
        led_vert.off()
        led_rouge.on()
        self.label_actif.config(text="Système desactivé", fg="red")
        self.btn_valider.config(state="disabled")