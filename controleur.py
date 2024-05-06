import LCD1602
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

buzzer = Buzzer(23)
led_rouge = LED(27)
led_vert = LED(22)
LCD1602.init(0x3f, 1)


class Controleur:
    def __init__(self, p_modele, p_vue):
        self.modele = p_modele
        self.vue = p_vue
        
    