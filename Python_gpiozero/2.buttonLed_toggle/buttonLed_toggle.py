from gpiozero import LED,Button
from time import sleep

led=LED(8)
btn=Button(25)
state=1
while True:
        if btn.is_pressed:
                #버튼 눌림
                if state==0:
                        state=1
                        led.on()

                else:
                        state=0
                        led.off()
                while btn.is_pressed:
                        sleep(0.1)
