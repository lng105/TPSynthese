import LCD1602, threading, datetime
import RPi.GPIO as GPIO
import KeypadGPIO as c
import tkinter as tk
from tkinter import ttk
from gpiozero import LED, MotionSensor, Buzzer
from time import sleep
from threading import Timer

LIGNES = 4
COLONNES = 4
lignesGPIO = [21, 20, 16, 12]
colonnesGPIO = [26, 19, 13, 6]

touches = ['1', '2', '3', 'A',
           '4', '5', '6', 'B',
           '7', '8', '9', 'C',
           '*', '0', '#', 'D']

pir = MotionSensor(25)
buzzer = Buzzer(23)
led_rouge = LED(27)
led_vert = LED(22)
LCD1602.init(0x3f, 1)
event_date = datetime.datetime.now()

class Controleur:
    def __init__(self, p_modele, p_vue):
        self.modele = p_modele
        self.vue = p_vue
        self.stop_event = threading.Event()
        self.correct_code = "5629"
        self.input_code = ""
        self.attempts = 0
        self.max_attempts = 3
        
    def update_journal_listbox(self, datetime_value, p_typeEvenement,p_valeurEvenement = None):
        date = datetime_value.strftime("%Y-%m-%d %H:%M:%S")
        self.modele.typeEvenement = p_typeEvenement
        self.modele.valeurEvenement = p_valeurEvenement
        message = f"{date} - {p_typeEvenement}"
        self.vue.journal_listbox.insert(tk.END, message)

    def start_system(self):
        led_vert.on()
        led_rouge.off()
        self.stop_event.clear()
        self.attempts = 0
        self.update_journal_listbox(event_date, "Activation du systeme d'alarme")

        def motion_buzzer():
            while not self.stop_event.is_set():
                pir.wait_for_motion()
                if self.stop_event.is_set():
                    break
                valeurEvenement = pir.value 
                LCD1602.write(0, 0, "Enter code ")
                buzzer.on()
                timer = Timer(2, buzzer.off)
                timer.start()
                timer.join()
                while not self.stop_event.is_set():
                    sleep(0.1)

        def input_lcd():
            clavier = c.Keypad(touches, lignesGPIO, colonnesGPIO, LIGNES, COLONNES)
            clavier.setDebounceTime(50)
            while not self.stop_event.is_set():
                touche = clavier.getKey()
                if touche != clavier.NULL:
                    if len(self.input_code) < 4:
                        self.input_code += touche
                        LCD1602.clear()
                        LCD1602.write(0, 0, "Enter code: " + self.input_code)

        self.buzzer_thread = threading.Thread(target=motion_buzzer, daemon=True)
        self.lcd_thread = threading.Thread(target=input_lcd, daemon=True)

        self.buzzer_thread.start()
        self.lcd_thread.start()

    def stop_system(self):
        self.stop_event.set()
        led_vert.off()
        led_rouge.on()
        buzzer.off()
        LCD1602.clear()
        self.update_journal_listbox(event_date, "Desactivation du systeme d'alarme")

        self.buzzer_thread.join()
        self.lcd_thread.join()

    def validate_code(self):
        if self.input_code == self.correct_code:
            self.input_code = ""
            self.attempts = 0
            LCD1602.write(0, 1, "Acces Valide")
            self.vue.disable_valider_button()
            self.update_journal_listbox(event_date, "Acces valide du systeme d'alarme")
            buzzer.off()
            led_vert.off()
            for _ in range(3):
                led_vert.on()
                sleep(0.2)
                led_vert.off()
                sleep(0.2)
            led_vert.on()
            return True
        else:
            self.input_code = ""
            self.attempts += 1
            if self.attempts == 1:
                buzzer.on()
                self.buzzer_timer = Timer(10, buzzer.off)
                self.buzzer_timer.start()
            if self.attempts >= self.max_attempts:
                self.vue.disable_valider_button()
                LCD1602.clear()
                self.update_journal_listbox(event_date, "Acces invalide du systeme d'alarme")
                LCD1602.write(0, 0, "Access Bloque")
                led_vert.off()
                for _ in range(10):
                    led_rouge.on()
                    sleep(0.2)
                    led_rouge.off()
                    sleep(0.2)
            else:
                LCD1602.clear()
                LCD1602.write(0, 0, f"Ressayer: {self.attempts}/{self.max_attempts}")
            return False
        
    def saveModele(self, p_typeEvenement,p_valeurEvenement=None):
        self.modele.typeEvenement = p_typeEvenement
        self.modele.valeurEvenement = p_valeurEvenement
        self.modele.saveFichier()