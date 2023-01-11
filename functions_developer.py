import pyautogui


def start_script_timer():
    print('Ready in 5 seconds.')
    pyautogui.sleep(1)
    print('- 4 sec.')
    pyautogui.sleep(1)
    print('- 3 sec.')
    pyautogui.sleep(1)
    print('- 2 sec.')
    pyautogui.sleep(1)
    print('- 1 sec.')
    pyautogui.sleep(1)
    print('Start')


def mouse_position():
    print(pyautogui.position())


def screen_shoot():
    print('Make ScreenShoot.')
#    lock_red_icons = pyautogui.screenshot('lock_red_icons.png', region=(1500,170, 60,210))       # Lock Red Icons
    ships_pictogram = pyautogui.screenshot('ships_pictograms.png', region=(1120, 15, 350, 100))





#screen_shoot()
#mouse_position()
