# 🟢 1. 버튼이 눌린 동안만 LED 켜기

## ✅ 설명  
이 프로젝트는 버튼이 **눌려 있는 동안만** LED가 켜지고,  
버튼에서 손을 떼면 자동으로 꺼지는 구조입니다.

- 버튼이 눌리면 `led.on()`
- 버튼이 떼지면 `led.off()`

---

## 📷 회로도  
![alt text](4bit.jpg)

---

## 🔌 핀 연결

| 구성품 | BCM 핀 번호 | 설명        |
|--------|-------------|-------------|
| LED    | 8           | LED 출력 핀 |
| 버튼   | 25          | 입력 버튼 핀 (내부 PULLUP 사용) |

---

## 🧠 코드

```python
from gpiozero import LED, Button
from time import sleep

led = LED(8)
btn = Button(25)

while True:
    if btn.is_pressed:
        led.on()
    else:
        led.off()
