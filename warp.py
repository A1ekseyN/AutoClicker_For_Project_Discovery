import pyautogui
from datetime import datetime, timedelta
from functions import global_timer_sec_to_minutes
from pictures import sun_png, warp_anomaly_0_png, warp_to_70_png, warping_png, speed_0_png


def check_ship_in_warp_or_not():
    # Проверка находится корабль в варпе или нет.
    while pyautogui.locateOnScreen(warping_png, confidence=0.9):
        print('Warping...')
        pyautogui.sleep(5)
    print('\nLanding...')


def warp_sun_to_70km():
    pyautogui.sleep(10)
    if pyautogui.locateOnScreen(sun_png, confidence=0.9):
        pyautogui.moveTo(pyautogui.locateOnScreen(sun_png, confidence=0.9))
        pyautogui.sleep(0.2)
        pyautogui.rightClick()
        pyautogui.moveTo(pyautogui.locateOnScreen(warp_anomaly_0_png, confidence=0.9))
        pyautogui.sleep(0.2)
        pyautogui.click(pyautogui.locateOnScreen(warp_to_70_png, confidence=0.9))
        print('\n--- Sun 70 km warping ---')
        pyautogui.sleep(60)
        pyautogui.moveTo(1200,350, 1)
        pyautogui.doubleClick()

        # TODO: После того, как корабль прилетел на солнце.
        #  Добавить раз в минуту анализ новых аномалий в системе.

        start_sun_time = datetime.now().timestamp()

        print(f'- Ship landing in the sun at: {datetime.now()}')
        ask = input('\nShip on sun. To continue, press any key...\n>>> ')
        sun_time = datetime.now().timestamp() - start_sun_time
        print(f'\n- Ship is in the sun {global_timer_sec_to_minutes(sun_time)}.')
    else:
        print('No sun in space.')
