# domino4 - 도미노 LED 점등

이 스크립트는 Raspberry Pi의 GPIO를 이용하여 4개의 LED가 차례대로 켜지고 꺼지는 **도미노 효과**를 연출합니다.

---

## 🔗 시연 영상

[YouTube 영상 링크](https://youtu.be/your-video-link)  


---

## ⚙️ 동작 설명

- 4개의 GPIO 핀을 **출력 모드**로 설정한 뒤,
- LED를 순서대로 `HIGH → 1초 대기 → LOW → 다음 LED` 방식으로 점등합니다.
- 무한 루프 구조로 계속 반복됩니다.

---

## 🧠 사용 핀 (GPIO)

| LED 순서 | GPIO | 핀 번호 (Header 기준) | 설명            |
|----------|------|------------------------|-----------------|
| 1        | 12   | 32번                   | 첫 번째 LED     |
| 2        | 16   | 36번                   | 두 번째 LED     |
| 3        | 20   | 38번                   | 세 번째 LED     |
| 4        | 21   | 40번                   | 네 번째 LED     |
| GND      | GND  |                        | 공통 GND 연결    |

---

## 💡 회로 구성

- 각 GPIO 핀 → 220Ω 저항 → LED 애노드(+)  
- LED 캐소드(-)는 GND로 연결  
- 각 LED는 개별적으로 점등/소등됨

### 📷 회로도 이미지
![KakaoTalk_20250408_160322183](https://github.com/user-attachments/assets/3c24febc-80eb-4316-8174-8db1ec8132ab)

---

## 📄 스크립트 코드 예시

```bash
#!/bin/bash

# 사용할 GPIO 번호들
pins=(12 16 20 21)

# 모든 핀을 출력 모드로 설정
for pin in "${pins[@]}"; do
  pinctrl set $pin op
done

# 무한 반복: LED를 순차적으로 켜고 끔
while true; do
  for pin in "${pins[@]}"; do
    pinctrl set $pin dh  # 켜기
    sleep 1
    pinctrl set $pin dl  # 끄기
  done
done
