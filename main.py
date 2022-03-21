import time
import pyautogui

print(pyautogui.position())

for i in range(1, 10): # 최대 10 챕터 정도 있다고 대충 생각하고 돌림
    for i in range(1, 30): # 한 챕터에 30 화면 정도 있다고 가정
        # 다음 버튼의 위치 구하기
        print(pyautogui.position())
        pyautogui.click(903, 181) #포커싱
        pyautogui.click(978, 706) #다음 버튼 클릭

        time.sleep(5) # 다음화면으로 넘어가는 중
        pyautogui.click(516, 384) # 재생 버튼 클릭

        time.sleep(60 * 3) # 영상 재생 완료 대기 (최대 3분정도로 잡음)

    # # 종료된 경우 닫고 새로운 영상 틈
    time.sleep(10)
    pyautogui.click(14, 53) # 닫기

    # 원래는 이미지 캡쳐 사용하여 종료 여부 판단하려 했음
    # 컴퓨터 껐다 켜야 한대서 안함.
    # img_capture = pyautogui.locateOnScreen("end-alert.png", confidence=0.7) # 70%
    # pyautogui.moveTo(img_capture)

    # 강의실 홈 화면으로 이동
    # print(pyautogui.position())
    pyautogui.click(858, 881) #포커싱
    pyautogui.hotkey('command', 'r') # 새로고침

    # 기다렸다가 학습하기 버튼 누름
    time.sleep(10)
    pyautogui.click(1033, 583)

    # 기다렸다가 확인 창 닫기
    time.sleep(5)
    pyautogui.click(615, 819)

    # 지니어스 홈
    # pyautogui.click(1548, 966) #포커싱
    # pyautogui.hotkey('command', 'r') # 새로고침

    # time.sleep(1800)