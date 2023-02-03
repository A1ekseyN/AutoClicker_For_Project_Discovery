import pyautogui


def lock_ship_ctrl_click():
    # Lock в прицел корабля
    pyautogui.press('ctrl')
    pyautogui.click()


def reload_guns():
    print('Reloading Guns.')
    pyautogui.keyDown('ctrl')
    pyautogui.sleep(0.1)
    pyautogui.press('r')
    pyautogui.sleep(0.1)
    pyautogui.keyUp('ctrl')

