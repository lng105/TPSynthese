from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(25)
led = LED(27)

while True:
    if pir.value == 1:
        led.on()
        print("1")
    else:
        led.off()
        print("2")
