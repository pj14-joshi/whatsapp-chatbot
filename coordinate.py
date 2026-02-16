import pyautogui, time

while True:
    a, b = pyautogui.position()
    print(a, b, end='\r')   # updates on same line
    time.sleep(0.1)
869 , 269
1596 , 1000
1052 , 1010