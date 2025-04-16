# 🔵 3. 버튼이 눌리면 domino4 1회 실행하기
https://youtu.be/huLmzw4uBc0?feature=shared

## ✅ 설명  
이 프로젝트는 버튼이 눌리면 **도미노처럼 4개의 LED가 순서대로 1초 간격으로 켜졌다 꺼지는** 애니메이션을 한 번 실행합니다.

- 누르면 `LED 1 → LED 2 → LED 3 → LED 4` 순으로 1초씩 켜졌다 꺼짐
- 누르고 있는 동안 여러 번 반복되지는 않음 (빠르게 눌러야 한 번씩 실행됨)

---

## 📷 회로도  
![alt text](4bit.jpg)

---

## 🔌 핀 연결

| LED 번호 | BCM 핀 번호 |
|----------|-------------|
| LED 1    | 8           |
| LED 2    | 7           |
| LED 3    | 16          |
| LED 4    | 20          |
| 버튼     | 25          |

---

## 🧠 코드

```python
from gpiozero import Button, LED
from time import sleep

pins = [8, 7, 16, 20]
leds = [LED(pin) for pin in pins]

btn = Button(25)

while True:
    if btn.is_pressed:
        for i in leds:
            i.on()
            sleep(1)
            i.off()
