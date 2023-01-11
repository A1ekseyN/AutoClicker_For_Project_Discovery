import pyautogui


def drones_start():
    print('--- Drones start ---')
    pyautogui.sleep(0.2)
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.sleep(0.3)
    pyautogui.keyUp('shift')


def drone_in_bay():
    print('--- Drones in bay ---')
    pyautogui.keyDown('shift')
    pyautogui.press('r')
    pyautogui.sleep(0.3)
    pyautogui.keyUp('shift')
