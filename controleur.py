import LCD1602, threading
import RPi.GPIO as GPIO
import KeypadGPIO as c
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

pir = MotionSensor(25)
buzzer = Buzzer(23)
led_rouge = LED(27)
led_vert = LED(22)
LCD1602.init(0x3f, 1)

class Controleur:
    def __init__(self, p_modele, p_vue):
        self.modele = p_modele
        self.vue = p_vue
        
    def start_system(self):
        led_vert.on()
        led_rouge.off()
        
        def motion_buzzer():
            while True:
                pir.wait_for_motion()
                LCD1602.write(0, 0, "Enter code ")
                buzzer.on()

        def input_lcd():
            position = 11
            clavier = c.Keypad(touches, lignesGPIO, colonnesGPIO, LIGNES, COLONNES)
            clavier.setDebounceTime(50)
            while True:
                touche = clavier.getKey()
                if touche != clavier.NULL:
                    if position == 15:
                        LCD1602.write(0, 2, "BOUTON VALIDER")
                    LCD1602.write(position, 0, touche)
                    position += 1
            
        threading.Thread(target = motion_buzzer, daemon = True).start()
        threading.Thread(target = input_lcd, daemon = True).start()

    def stop_system(self):
        led_vert.off()
        led_rouge.on()
        buzzer.off()
        LCD1602.clear()