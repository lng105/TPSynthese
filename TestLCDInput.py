import LCD1602
import RPi.GPIO as GPIO
import KeypadGPIO as c

LIGNES = 4
COLONNES = 4

touches = ['1','2','3','A',
           '4','5','6','B',
           '7','8','9','C',
           '*','0','#','D']

lignesGPIO = [21,20,16,12]
colonnesGPIO = [26,19,13,6]

def initLCD():
    LCD1602.init(0x3f, 1)

def affichageToucheEcran():
    clavier = c.Keypad(touches, lignesGPIO, colonnesGPIO, LIGNES, COLONNES)
    clavier.setDebounceTime(50)
    while True:
        touche = clavier.getKey()
        if(touche != clavier.NULL):
            LCD1602.write(0,0, touche)
            print("Touche : %c "%(touche))
            
if __name__ == '__main__':
    print("Demarrage du programme... ")
    try:
        initLCD()
        affichageToucheEcran()
    except KeyboardInterrupt:
        GPIO.cleanup()

