# domino4

LED 제어 스크립트로, Raspberry Pi의 GPIO 핀을 사용하여 3개의 LED를 이진법으로 점등합니다.  
예: 1 → 001, 2 → 010, 3 → 011, ..., 7 → 111  
GPIO 핀 12, 16, 20번을 사용합니다.

## 🔗 시연 영상

[YouTube 영상 링크](https://youtu.be/your-video-link)  


## 💡 회로 구성

- 사용 핀: GPIO 12, 16, 20
- 각 GPIO는 220Ω 저항을 통해 LED의 애노드(+)에 연결되며, 캐소드(-)는 GND와 연결됩니다.
- LED 순서:
  - GPIO 12 → 최하위 비트 (LSB)
  - GPIO 16 → 중간 비트
  - GPIO 20 → 최상위 비트 (MSB)

### 핀맵 예시 (왼쪽이 라즈베리파이 핀 번호, 오른쪽은 연결)

| GPIO 번호 | 핀 번호 | 용도       |
|-----------|---------|------------|
| GPIO12    | 32번    | LSB LED    |
| GPIO16    | 36번    | MID LED    |
| GPIO20    | 38번    | MSB LED    |
| GND       | 6번     | 모든 LED의 GND |

### 회로도 이미지  
![KakaoTalk_20250408_160322183_01](https://github.com/user-attachments/assets/e580c678-2405-4b2a-9f6c-c01c9df528a3)


## 🧠 코드 설명

### 사용한 Bash 스크립트 구조 요약

```bash
#!/bin/bash

# 사용할 GPIO 핀 배열
pins=(12 16 20)

# 핀들을 출력 모드로 설정
for pin in "${pins[@]}"; do
  pinctrl set $pin op
done

# 0~7까지 이진법으로 카운팅하여 LED 점등
while true; do
  for n in {0..7}; do
    for i in {0..2}; do
      bit=$(( (n >> i) & 1 ))
      if [ "$bit" -eq 1 ]; then
        pinctrl set ${pins[$i]} dh
      else
        pinctrl set ${pins[$i]} dl
      fi
    done
    sleep 1
  done
done
