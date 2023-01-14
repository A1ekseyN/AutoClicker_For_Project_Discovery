# Version: 0.0.2a
from datetime import datetime, timedelta
import pyautogui
from pictures import *


### Алгоритм старта Abyss
#+ ПКМ
#+ Курсор на -> Места
#+ Курсор на -> Spots
#+ Курсор на -> Spot
#+ Клик по -> Варп в 70.
#+ Клик по -> Hold (Инвентарь)
#+ ПКМ по -> Exotic Filament
#+ Клик по Использовать Exotic Filament
# Клик по "Активировать для флота"
#+ Клик по Воротам
#+ Press 'd'
#+ Клик по "Активировать"

print('Start in 5 seconds.')
pyautogui.sleep(5)

def start_first_abyss_t0_exotic():
    # Start Exotic T0 Abyss.
    start_time = datetime.now().timestamp()
#    pyautogui.sleep(5)
    print('Start Abyss Exotic T0.')
    pyautogui.moveTo(pyautogui.locateOnScreen(hold_icon_png, confidence=0.9))
    print(pyautogui.locateOnScreen(hold_icon_png, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.click()
    pyautogui.sleep(0.2)
    pyautogui.moveTo(pyautogui.locateOnScreen(abyss_filament_exotic_t0_icon_png, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.rightClick()
    pyautogui.sleep(0.2)
    pyautogui.moveTo(pyautogui.locateOnScreen(use_exotic_filament, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.click()
    print('Activation for fleet. Sleep 7 sec.')
    pyautogui.sleep(7)
    pyautogui.moveTo(pyautogui.locateOnScreen(abyss_activate_for_fleet, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.click()
    print('Sleep 7 sec.')

    pyautogui.sleep(7)
    pyautogui.moveTo(pyautogui.locateOnScreen(abyss_gate_icon_png, confidence=0.8))
    print(f'Locate Abyssal Icon: {pyautogui.locateOnScreen(abyss_gate_icon_png, confidence=0.8)}')
    pyautogui.sleep(0.2)
    pyautogui.click()

    pyautogui.moveTo(pyautogui.locateOnScreen(abyssal_trace_png, confidence=0.9))
    print(f'Locate Abyssal Trace: {pyautogui.locateOnScreen(abyssal_trace_png, confidence=0.9)}')
    pyautogui.sleep(0.2)
    pyautogui.click()

    pyautogui.sleep(3)
    print('Sleep 3 sec.')
#    pyautogui.click()
#    pyautogui.sleep(0.2)
    pyautogui.press('d')
    pyautogui.sleep(0.2)            # Скорее всего, тут нужен больше sleep
    pyautogui.moveTo(pyautogui.locateOnScreen(filament_activate_icon_png, confidence=0.9))
    pyautogui.sleep(1)
    pyautogui.click()

    # Закрыть инвентарь
    pyautogui.sleep(1)
    print('Close Window.')
    pyautogui.moveTo(pyautogui.locateOnScreen(window_close_png, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.click()

    # Активировать через ворота
    print('Abyss Exotic filament T0 - use.')
    print(f'Time: {round(datetime.now().timestamp() - start_time):,.2f} sec.')


def warp_spot_0():
    # Warp на Spot через ПКМ
    pyautogui.moveTo(750, 500, 1)
    pyautogui.rightClick()
    pyautogui.sleep(0.2)
    places_icon = pyautogui.locateOnScreen(places_icon_png, confidence=0.9)
    #    places_icon = pyautogui.locateOnScreen('pics_bot/warp/places.png')
    #    print(places_icon)
    pyautogui.moveTo(places_icon)
    #    pyautogui.moveTo(places_icon_png, confidence=0.9)
    pyautogui.sleep(0.2)
    pyautogui.moveTo(pyautogui.locateOnScreen(spots_icon_png, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.moveTo(pyautogui.locateOnScreen(spot_01_icon_png, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.moveTo(pyautogui.locateOnScreen(warp_to_0, confidence=0.9))
    pyautogui.sleep(0.2)
    pyautogui.click()
    print('Warp to Spot - 0 km.')


def abyss_exotic_t0():
    # Exotic T0
    # Sparkneedle Tessera - Стандарт. Отправить дронов, они сами разберутся.
    # Strikeneedle Tessera - Стандарт.
    # Ephialtes Lanced - Стандарт.
    # Emberlance Tessera - Стандарт
    # Ударный "Домовой"
    # Lucid Aegis

    # Triglavian Biocom - Контейнер.
    # Остров Triglavian - Drop
    # Transfer Conduit - Выход из abyss

    # Нет скрина
    # Bless...
    # Attacer Pacifier
    # Stormbringer
    pass


def abyss_go_to_gate():
    abyss_gate_button = pyautogui.locateOnScreen(abyss_gate_png, confidence=0.9)
    pyautogui.moveTo(abyss_gate_button)
    pyautogui.sleep(0.2)
    pyautogui.click


def abyss_lock_container():
    abyss_container_button = pyautogui.locateOnScreen(abyss_container_png, confidence=0.8)
    pyautogui.click(abyss_container_button)


#warp_spot_0()
start_first_abyss_t0_exotic()
#abyss_go_to_gate()
exit = input('For exit press any key.')
