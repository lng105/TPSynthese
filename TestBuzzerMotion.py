from gpiozero import Buzzer, MotionSensor
import time

pir = MotionSensor(25)
buzzer = Buzzer(23)

code_entre = "1234"  # Example code
code_tape = ""

def on_motion():
    print("Motion detected")
    buzzer.on()
    code = input("Enter code to deactivate buzzer: ")
    if code == code_entre:
        buzzer.off()
        print("Buzzer deactivated")
    else:
        print("Incorrect code. Try again.")

def on_no_motion():
    print("No motion detected")
    buzzer.off()

pir.when_motion = on_motion
pir.when_no_motion = on_no_motion

while True:
    time.sleep(1)
