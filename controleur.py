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
        self.stop_event = threading.Event()
        self.correct_code = "1234"  # Example correct code
        self.input_code = ""
        
    def start_system(self):
        led_vert.on()
        led_rouge.off()
        self.stop_event.clear()
        
        def motion_buzzer():
            while not self.stop_event.is_set():
                pir.wait_for_motion()
                if self.stop_event.is_set():
                    break
                LCD1602.write(0, 0, "Enter code ")
                buzzer.on()
                while not self.stop_event.is_set():
                    sleep(0.1)
        
        def input_lcd():
            position = 11
            clavier = c.Keypad(touches, lignesGPIO, colonnesGPIO, LIGNES, COLONNES)
            clavier.setDebounceTime(50)
            while not self.stop_event.is_set():
                touche = clavier.getKey()
                if touche != clavier.NULL:
                    if len(self.input_code) < 4:
                        self.input_code += touche
                        LCD1602.write(position, 0, touche)
                        position += 1
            
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

        self.buzzer_thread.join()
        self.lcd_thread.join()
        
    def validate_code(self):
        if self.input_code == self.correct_code:
            self.input_code = ""
            buzzer.off()
            LCD1602.clear()
            return True
        else:
            self.input_code = ""
            return False
