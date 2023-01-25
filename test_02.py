from pictures import *
import pyautogui
from datetime import datetime, timedelta


start_time = datetime.now().timestamp()
region = (1120, 15, 350, 100)

if pyautogui.locateOnScreen(frigate_01_png, confidence=0.9):
    print('On screen')
else:
    print('Not in screen')


print(pyautogui.position())
a = pyautogui.position()[0] - 25
b = pyautogui.position()[1] + 5
#a = pyautogui.Point(x=-30, y=0)
print(a)
pyautogui.moveTo(a, b, 0.2)

#if pyautogui.locateOnScreen(frigate_red_png):
#    print('On screen')
#else:
#    print('Not in screen')

print(datetime.now())
print(datetime.now().timestamp() - start_time)
