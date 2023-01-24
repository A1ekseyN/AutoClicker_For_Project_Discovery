# Version 0.0.1yh
print('Version: 0.0.1yh')


import os
import pyautogui
from datetime import datetime, timedelta
#from abyss import *
from drones import *
from functions import *
from functions_developer import start_script_timer
from pictures import *
from settings import *
from warp import *


#pyautogui.alert('For Start script press OK.')

start_script_timer()

start_time_global = datetime.now().timestamp()


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


def lock_enemy_ships():
    start_time = datetime.now().timestamp()
    if check_ships():
        region = (1500,170, 60,210)
        pyautogui.sleep(0.2)
        frigate_search = pyautogui.locateAllOnScreen(frigate_red_png, confidence=0.85, region=region)
        if frigate_search:
            for frigate in frigate_search:
                print('- Lock Frigate')
                pyautogui.click(frigate)
                pyautogui.click(frigate)
                lock_ship_ctrl_click()
            pyautogui.press('f')

        frigate_search_box_red = pyautogui.locateAllOnScreen(frigate_red_box_red_png, confidence=0.85, region=region)
        if frigate_search_box_red:
            for frigate in frigate_search_box_red:
                print('- Lock Frigate Red Box')
                pyautogui.click(frigate)
                pyautogui.click(frigate)
                lock_ship_ctrl_click()

#        pyautogui.press('f')
        frigate_search_box_yellow = pyautogui.locateAllOnScreen(frigate_red_box_yellow_png, confidence=0.85, region=region)
        if frigate_search_box_yellow:
            for frigate in frigate_search_box_yellow:
                print('- Lock Frigate Yellow Box -')
                pyautogui.click(frigate)
                pyautogui.click(frigate)
                lock_ship_ctrl_click()

        destroyer_search = pyautogui.locateAllOnScreen(destroyer_red_png, confidence=0.85, region=region)
        if destroyer_search:
            for destroyer in destroyer_search:
                print('- Lock Destroyer')
                pyautogui.click(destroyer)
                pyautogui.click(destroyer)
                lock_ship_ctrl_click()

        destroyer_search_box_red = pyautogui.locateAllOnScreen(destroyer_red_box_png, confidence=0.85, region=region)
        if destroyer_search_box_red:
            for destroyer in destroyer_search_box_red:
                print('- Lock Destroyer Box Red')
                pyautogui.click(destroyer)
                pyautogui.click(destroyer)
                lock_ship_ctrl_click()

        cruiser_search = pyautogui.locateAllOnScreen(cruiser_red_png, confidence=0.85, region=region)
        if cruiser_search:
            for cruiser in cruiser_search:
                print('- Lock Cruiser')
                pyautogui.click(cruiser)
                pyautogui.click(cruiser)
                lock_ship_ctrl_click()
            pyautogui.press('f')

        cruiser_search_box_red = pyautogui.locateAllOnScreen(cruiser_red_box_red_png, confidence=0.85, region=region)
        if cruiser_search_box_red:
            for cruiser in cruiser_search_box_red:
                print('- Lock Cruiser')
                pyautogui.click(cruiser)
                pyautogui.click(cruiser)
                lock_ship_ctrl_click()

        tower_search = pyautogui.locateAllOnScreen(tower_red_png, confidence=0.85, region=region)
        if tower_search:
            for tower in tower_search:
                print('- Lock Tower')
                pyautogui.click(tower)
                pyautogui.click(tower)
                lock_ship_ctrl_click()

        pyautogui.press('f')
        tower_search_box_red = pyautogui.locateAllOnScreen(tower_red_box_png, confidence=0.85, region=region)
        if tower_search_box_red:
            for tower in tower_search_box_red:
                print('- Lock Tower')
                pyautogui.click(tower)
                pyautogui.click(tower)
                lock_ship_ctrl_click()
        pyautogui.press('f')
        print(f'Locking ships: {datetime.now().timestamp() - start_time:,.2f} sec.')
        search_enemy_ships_pictograms()
    else:
        print(f'Locking ships: {datetime.now().timestamp() - start_time:,.2f} sec.')
        print('- Ships not found')
        pyautogui.sleep(1)


def search_enemy_ships_pictograms():
    # Поиск иконок кораблей в верхней части экрана
    start_time = datetime.now().timestamp()
    region = (1120, 15, 350, 100)
#    region = (1136, 15, 1452, 113)     # Old Slow
#1 ship - region=(1346,15, 1452, 113)
#2 ships -  region=(1240,15, 1452, 113)
#3 ships - region=(1136,15, 1452, 113)
#4 ship - region=(1021,15, 1452, 113)
#5 ships - region=(914,15, 1452, 113)

    try:
        pictogram_hp_full_01 = pyautogui.locateOnScreen(hp_full_01, confidence=0.85, region=region)
        if pictogram_hp_full_01:
            print('Detected - HP Full')
            pyautogui.moveTo(pictogram_hp_full_01)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error. HP Full 01.')

    try:
        pictogram_frigate_01 = pyautogui.locateOnScreen(frigate_01_png, confidence=0.85, region=region)
        if pictogram_frigate_01:
            print('Detected - Frigate 01.')
            pyautogui.moveTo(pictogram_frigate_01)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error. Frigate 01.')

    try:
        pictogram_frigate_02 = pyautogui.locateOnScreen(frigate_02_png, confidence=0.85, region=region)
        if pictogram_frigate_02:
            print('Detected - Frigate 02.')
            pyautogui.moveTo(pictogram_frigate_02)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error. Frigate 02.')

    try:
        pictogram_frigate_03 = pyautogui.locateOnScreen(frigate_03_png, confidence=0.85, region=region)
        if pictogram_frigate_03:
            print('Detected - Frigate 03.')
            pyautogui.moveTo(pictogram_frigate_03)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error - Frigate 03.')

    try:
        pictogram_frigate_04 = pyautogui.locateOnScreen(frigate_04_png, confidence=0.85, region=region)
        if pictogram_frigate_04:
            print('Detected - Frigate 04.')
            pyautogui.moveTo(pictogram_frigate_04)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error - Frigate 04.')

    try:
        pictogram_frigate_05 = pyautogui.locateOnScreen(frigate_05_png, confidence=0.85, region=region)
        if pictogram_frigate_05:
            print('Detected - Frigate 05.')
            pyautogui.moveTo(pictogram_frigate_05)
            pyautogui.press('f')
            pyautogui.press('f1')
    except:
        print('Pictogram error - Frigate 05.')

    print(f'Pictogram Time: {datetime.now().timestamp() - start_time:,.2f} sec.')
    pyautogui.sleep(0.1)


def take_drop_in_space():
    print('--- Take Drop ---')
    go_to_drop_search = pyautogui.locateOnScreen(loot_in_space_png, confidence=0.9)
    pyautogui.moveTo(go_to_drop_search)
    pyautogui.click()
    pyautogui.sleep(0.5)
    approach_search = pyautogui.locateOnScreen(approach_png, confidence = 0.7)
    pyautogui.moveTo(approach_search)
    pyautogui.click()
    pyautogui.sleep(1)
    drop_box_search = pyautogui.locateOnScreen(drop_box_png, confidence=0.9)
    pyautogui.moveTo(drop_box_search)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(0.5)
    take_loot_search = pyautogui.locateOnScreen(take_loot_png, confidence=0.9)
    pyautogui.moveTo(take_loot_search)
    pyautogui.sleep(0.5)
    pyautogui.click(take_loot_search)


def warp_next_anomaly():
    cnt = 0
    anomaly_search = pyautogui.locateOnScreen(warp_to_anomaly_green_icon_png, confidence = 0.8)
    if anomaly_search:
        print('\n--- Warp in anomaly ---')
        pyautogui.moveTo(anomaly_search)
        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.sleep(3)

        while check_ships() == None:
            pyautogui.sleep(10)
            print('\nWarping...')
            cnt += 1
            print(f'Warp conter: {cnt}.')
            if cnt == 6:
                print('-- Break Warp !!! ---')
                break
        print('Landing...\n')
    else:
        print('\n- No anomalies in space.')
        pyautogui.sleep(1)


def warp_anomaly_context_menu():
    # Функция для варпа через ПКМ или контектсное меню.
    pyautogui.sleep(0.2)
    pyautogui.click(button='RIGHT')
    pyautogui.sleep(0.2)
    try:
        pyautogui.locateOnScreen(warp_anomaly_0_png, confidence=0.8)
        pyautogui.moveTo(warp_anomaly_0_png)
        pyautogui.sleep(0.2)
        pyautogui.click()
        print('\nWait 10 sec after start warping.')
        pyautogui.sleep(10)
    except:
        print('No warp button.')
        check_battle()


def warp_green_anomaly_context_menu():
    # Guristas Укрытие (Hideaway)
    start_time = datetime.now().timestamp()

    guristas_hideaway = pyautogui.locateOnScreen(guristas_hideaway_name_png, confidence=0.95)
    guristas_hideaway_new = pyautogui.locateOnScreen(guristas_hideaway_new_name_png, confidence=0.9)
    guristas_refuge = pyautogui.locateOnScreen(guristas_refuge_name_png, confidence=0.9)
    guristas_refuge_new = pyautogui.locateOnScreen(guristas_refuge_new_name_png, confidence=0.9)
    guristas_den = pyautogui.locateOnScreen(guristas_den_name_png, confidence=0.9)
    guristas_den_new = pyautogui.locateOnScreen(guristas_den_name_new_png, confidence=0.9)

    guristas_anomalies = [guristas_hideaway, guristas_hideaway_new,
                          guristas_refuge, guristas_refuge_new,
                          guristas_den, guristas_den_new]

    for anomaly in guristas_anomalies:
        if anomaly:
            print(anomaly)
            pyautogui.moveTo(anomaly)
            warp_anomaly_context_menu()
#            print('\nWait 10 sec after start warping.')
#            pyautogui.sleep(10)
            break
    print(f'--- Guristas Anomaly Search: {datetime.now().timestamp() - start_time:,.2f} sec.')
    if not anomaly:
        next_gate()


def next_gate():
    # Warp next yellow gate
    print('\n--- Warp Next Gate ---')
    pyautogui.press('d')
    gate_next_search = pyautogui.locateOnScreen(gate_yellow_png, confidence=0.8)    #0.8
    print(gate_next_search)
    show_global_timer()
    if gate_next_search:
        pyautogui.moveTo(gate_next_search)
#        pyautogui.sleep(0.5)
        pyautogui.click()
        pyautogui.sleep(0.5)
        pyautogui.press('d')
        print('- Warping -')
        reload_guns()               # Перезарядка пушек
        pyautogui.moveTo(1000,500, 1)
        pyautogui.sleep(30)
        print('Warp - 30 sec left.')
        pyautogui.sleep(15)
        print('Warp - 15 sec left.\n')
        pyautogui.sleep(15)
        start_green_anomaly()
    else:
        pyautogui.sleep(1)
        go_in_gate_button = pyautogui.locateOnScreen(go_in_gate_png, confidence=0.7)    # Меньше confidence
#        go_in_gate_button = pyautogui.locateOnScreen(gate_yellow_png, confidence=0.8)    # Меньше confidence
        print(go_in_gate_button)
        if go_in_gate_button:
            pyautogui.click(go_in_gate_button)
            pyautogui.sleep(0.3)
            pyautogui.click()
            print(' -- Warp - Go in gate Icon -- ')
            pyautogui.sleep(60)
        else:
            warp_next_anomaly()
#            next_gate()
            if pyautogui.locateOnScreen(gate_yellow_png, confidence=0.8):
                next_gate()
            else:
                warp_sun_to_70km()


def check_battle():
    # Проверка или корабль находится в битве.
    print('\n--- Check Battle status ---')
    pyautogui.click(1000, 500)
    if check_ships():
        print('--- Ships Found. Start Battle. ---')
        drones_start()
        lock_enemy_ships()
        try:
            drones_check_hp()
        except:
            print('\n\tError Drone HP Function.')
        pyautogui.sleep(1)
        check_battle()
    else:
        pyautogui.sleep(5)
        if check_ships() == None:
#            pyautogui.sleep(0.5)
            print('--- Кораблей нет ---')
            drone_in_bay()
            # Тут можно сделать функцию, которая становится в разгон. В то время, пока ждем дронов.
            print('Wait for Drones - 5 sec.')
            pyautogui.sleep(5)


def check_ships():
#    region_rings_up = (1500, 190, 1560, 400)        # Нужно проверить, что это. Скорее всего Grid
    # Если нет region, то сканирует весь экран. Если два монитора, то с двух мониторов.
    start_time = datetime.now().timestamp()

    frigate_search = pyautogui.locateOnScreen(frigate_red_png, confidence=0.85)
    frigate_search_box_red = pyautogui.locateOnScreen(frigate_red_box_red_png, confidence=0.85)
    frigate_search_box_yellow = pyautogui.locateOnScreen(frigate_red_box_yellow_png, confidence=0.85)
    destroyer_search = pyautogui.locateOnScreen(destroyer_red_png, confidence=0.85)
    destroyer_search_box_red = pyautogui.locateOnScreen(destroyer_red_png, confidence=0.85)
#    destroyer_search_yellow_box = pyautogui.locateOnScreen(xxx, confidence=0.85, region=region)
    cruiser_search = pyautogui.locateOnScreen(cruiser_red_png, confidence=0.85)
    cruiser_search_red_box = pyautogui.locateOnScreen(cruiser_red_box_red_png, confidence=0.85)
#    cruiser_search_yellow_box = None
    tower_search = pyautogui.locateOnScreen(tower_red_png, confidence=0.85)
    tower_search_red_box = pyautogui.locateOnScreen(tower_red_box_png, confidence=0.85)
#    tower_search_yellow_box = None
    hp_full_02 = pyautogui.locateOnScreen(hp_full_02_png, confidence=0.85)
    hp_full_03 = pyautogui.locateOnScreen(hp_full_03_png, confidence=0.85)
    hp_full_04 = pyautogui.locateOnScreen(hp_full_04_png, confidence=0.85)

# TODO:
#    В данный момент лочит не только корабли, но и вреки.
#   Заменить картинки на картинки с названиями кораблей.
#    guristas_search_text_png = pyautogui.locateOnScreen(guristas_text_png, confidence=0.9)
#    pithior_search_text_png = pyautogui.locateOnScreen(frigate_guristas_pithior_text_png, confidence=0.9)
#    pithis_search_text_png = pyautogui.locateOnScreen(frigate_guristas_pithis_text_png, confidence=0.9)

#    tower_search_text_png = pyautogui.locateOnScreen(tower_text_png, confidence=0.9)

    if frigate_search or frigate_search_box_red or frigate_search_box_yellow \
        or destroyer_search or destroyer_search_box_red \
        or cruiser_search or cruiser_search_red_box\
        or tower_search or tower_search_red_box\
        or hp_full_02 or hp_full_03 or hp_full_04:
# Нужно заменить картинки с текстом, на полное название корабля или башни.
#        or guristas_search_text_png or pithior_search_text_png or pithis_search_text_png\
#        or tower_search_text_png:
        print('- Ship Find')
        print(f'Check ships All Screen: {datetime.now().timestamp() - start_time:,.2f} sec.')
        return True
    else:
        print('- No ships -')
        print(f'Check ships: {datetime.now().timestamp() - start_time:,.2f} sec.')
        return None


def check_anomaly():
    # Проверка или в системе есть аномалии.
    anomaly_search = pyautogui.locateOnScreen(warp_to_anomaly_green_icon_png, confidence = 0.8)
    if anomaly_search:
        print('- Найдены аномалии -')
        return True
    else:
        print('- Аномалий больше нет. -')
        return False

def show_global_timer():
    print(f'\n--- Global Timer: {global_timer_sec_to_minutes(datetime.now().timestamp() - start_time_global)}')

def start_green_anomaly():
    # Start Green Anomaly.
#    warp_next_anomaly()
    warp_green_anomaly_context_menu()
    check_ship_in_warp_or_not()                     # Test Need. Проверка или корабль находится в warp
    if check_battle():
        check_battle()
    if check_anomaly():
        print('- Следующая аномалия -')
        drone_in_bay()                              # На всякий пожарный еще раз собрать дронов
        start_green_anomaly()
    if check_anomaly() == False:
        next_gate()
        drone_in_bay()
    start_green_anomaly()


# Start Green Anomaly.
try:
    start_green_anomaly()
except:
    print('Error')
    input('Press key to exit.')


print('--- End Script ---')
print(f'\n--- Global Timer: {global_timer_sec_to_minutes(datetime.now().timestamp() - start_time_global)}')
a = input('Prees any key to exit.')
