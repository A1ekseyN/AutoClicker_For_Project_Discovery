# Version: 0.0.1o
import pyautogui
from datetime import datetime, timedelta
from pictures import *


def new_route_for_bot():
    # Прокладываем новый маршрут
    print('\nStart make new Route after 10 sec.')
    pyautogui.sleep(5)

    start_time = datetime.now().timestamp()
    solar_systems_list = ['aramachi', 'motsu', 'hitanishio', 'isikesu', 'oshaima', 'oisio', 'venilen',
                          'rairomon', 'eskunen', 'outuni', 'ichinumi', 'aokannitoh', 'kylmabe', 'mahtista',
                          'ahtulaima', 'vaankalen', 'jatate',
                          'liekuri', 'poinen', 'vahunomi', 'otitoh', 'airmia', 'uminas', 'wuos', 'nuken',
                          'reisen', 'purjola', 'hurtoken', 'saisio',
                          'soshin', 'ukkalen', 'akkilen',
                          'kaaputen', 'inari', 'sirppala',
                          'saila']

    print('\n--- Start Make New Route --- ')
    pyautogui.press('f10')
    print('Open map. Wait 10 sec.')
    pyautogui.sleep(10)


    def icon_map_search():
        # Ищем иконку лупы. (Поиска солнечной системы)
        icon_map_search = pyautogui.locateOnScreen(icon_map_search_png, confidence=0.9)
        pyautogui.moveTo(icon_map_search)
        pyautogui.click()
        pyautogui.sleep(0.2)


    def ctrl_a():
        # Выделяем написанный текст в поиске. Ctrl + A
        pyautogui.keyDown('ctrl')
        pyautogui.sleep(0.2)
        pyautogui.press('a')
        pyautogui.sleep(0.2)
        pyautogui.keyUp('ctrl')
        pyautogui.sleep(0.2)


    def set_route_first_system():
        # Первый пункт в маршруте
        for i in first_system_in_route:
            print(f'- {first_system_in_route}')
            icon_map_search()
            ctrl_a()

            for letter in i:
                pyautogui.press(letter)
                pyautogui.sleep(0.1)

            pyautogui.sleep(1)

            mouse_position_x = pyautogui.position()[0]
            mouse_position_y = pyautogui.position()[1] + 35
            pyautogui.moveTo(mouse_position_x, mouse_position_y, 0.2)
            pyautogui.rightClick()
            pyautogui.sleep(0.2)

            first_system = pyautogui.locateOnScreen(icon_set_route_png, confidence=0.9)
            pyautogui.moveTo(first_system)
            pyautogui.click()

#    set_route_first_system()

    cnt = 0
    for system_name in solar_systems_list:
        cnt += 1
        print(f'- {system_name} ({cnt} / {len(solar_systems_list)})')
        icon_map_search()
        ctrl_a()

        for letter in system_name:
            pyautogui.press(letter)
            pyautogui.sleep(0.1)

        # Ищем иконку солнечной системы + Кликаем по ней правой кнопкой и задаем маршрут
        region = (100, 100, 1000, 800)
        pyautogui.sleep(1)
        icon_solar_system = pyautogui.locateOnScreen(icon_solar_system_png, confidence=0.7, region=region)
        pyautogui.moveTo(icon_solar_system)

        # Переместить курсор на 35 пикселей вниз.
        mouse_position_x = pyautogui.position()[0]
        mouse_position_y = pyautogui.position()[1] + 35
        pyautogui.moveTo(mouse_position_x, mouse_position_y, 0.2)

        pyautogui.sleep(0.2)
        pyautogui.rightClick()
        pyautogui.sleep(0.2)
        icon_add_waypoint = pyautogui.locateOnScreen(icon_add_waypoint_png, confidence=0.9)
        pyautogui.moveTo(icon_add_waypoint)
        pyautogui.click()
        pyautogui.sleep(0.2)

        mouse_position_x = pyautogui.position()[0] - 25
        mouse_position_y = pyautogui.position()[1] + 5
        pyautogui.moveTo(mouse_position_x, mouse_position_y, 0.2)
        pyautogui.click()
        pyautogui.sleep(0.2)

    pyautogui.press('f10')
    print(f'\nRoute creation time: {datetime.now().timestamp() - start_time} sec.')

#new_route_for_bot()
