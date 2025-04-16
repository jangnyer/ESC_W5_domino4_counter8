from gpiozero import Button,LED
from time import sleep

pins=[8,7,16,20]
leds=[LED(pin) for pin in pins]

btn=Button(25)

while True:
        if btn.is_pressed:
                for i in leds:
                        i.on()
                        sleep(1)
                        i.off()