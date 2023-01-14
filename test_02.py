from pictures import *
import pyautogui
from datetime import datetime, timedelta


start_time = datetime.now().timestamp()
region = (1120, 15, 350, 100)

if pyautogui.locateOnScreen(frigate_01_png, confidence=0.9):
    print('On screen')
else:
    print('Not in screen')

#if pyautogui.locateOnScreen(frigate_red_png):
#    print('On screen')
#else:
#    print('Not in screen')


print(datetime.now().timestamp() - start_time)
