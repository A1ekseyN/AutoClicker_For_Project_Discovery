from datetime import datetime, timedelta
import pyautogui
from pictures import drone_hp_mid_png, drone_back_icon_png, drone_backing_text_png


def drones_start():
    print('--- Drones start ---')
    pyautogui.sleep(0.2)
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.press('п')
    pyautogui.sleep(0.2)
    pyautogui.keyUp('shift')


def drone_in_bay():
    print('--- Drones in bay ---')
    pyautogui.keyDown('shift')
    pyautogui.press('r')
    pyautogui.press('к')
    pyautogui.sleep(0.2)
    pyautogui.keyUp('shift')


def drones_check_hp():
#    print('Drones check HP.')
    start_time = datetime.now().timestamp()
    drone = pyautogui.locateOnScreen(drone_hp_mid_png, confidence=0.95)
    if drone:
        print(f'Back drone with Low Shield.')
        pyautogui.moveTo(drone)
        pyautogui.sleep(0.2)
        drone_back_icon = pyautogui.locateOnScreen(drone_back_icon_png, confidence=0.95)
        pyautogui.click(drone_back_icon)
        print(f'Drone Low HP check: {round(datetime.now().timestamp() - start_time):,.2f} sec.')
    print(f'Drone check HP: {round(datetime.now().timestamp() - start_time, 2):,.2f} sec.')
