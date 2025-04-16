from gpiozero import LED, Button
from signal import pause

# 4비트용 LED 연결
led0 = LED(8)   # LSB (2^0)
led1 = LED(7)   # 2^1
led2 = LED(16)  # 2^2
led3 = LED(20)  # MSB (2^3) — 추가 필요!

btn = Button(25)

count = 0  # 0~15 사이의 숫자를 저장하는 카운터 변수

# 숫자를 이진수로 변환해 LED로 표시하는 함수
def show_binary(n):
    led0.value = n & 0b0001
    led1.value = (n >> 1) & 0b0001
    led2.value = (n >> 2) & 0b0001
    led3.value = (n >> 3) & 0b0001

# 버튼이 눌렸을 때 호출되는 함수
def on_button_pressed():
    global count
    count = (count + 1) % 16  # 0~15까지 증가 후 다시 0으로
    show_binary(count)
    print(f"count = {count}")

# 버튼 눌렀을 때 이벤트 연결
btn.when_pressed = on_button_pressed

pause()  # 프로그램을 계속 실행시켜주는 대기 함수