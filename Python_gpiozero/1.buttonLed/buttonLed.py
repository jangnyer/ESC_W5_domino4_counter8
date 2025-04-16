from gpiozero import LED,Button
from time import sleep

led=LED(8)
btn=Button(25)

while True:
        if(btn.is_pressed):
                #버튼이 눌렸을때
                led.on()
        else:
                led.off()