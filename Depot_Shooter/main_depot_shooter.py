import time
import pyautogui
import cv2
import os
import numpy as np


def get_screenshot():
    """Функция для создания снимка экрана и возврата его как переменной"""
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    return screenshot_cv


def get_solar_system_and_depot_count(screen_image, images_folder='images/solar_systems', icons_folder='images/icons'):
    """Функция для проверки наличия совпадений с изображениями из папки"""
    search_area = cv2.cvtColor(screen_image[:500, :600], cv2.COLOR_BGR2GRAY)
    solar_check_time = time.time()

    system_name = None
    for system_image_file in os.listdir(images_folder):
        system_image_path = os.path.join(images_folder, system_image_file)
        system_image = cv2.imread(system_image_path, cv2.IMREAD_GRAYSCALE)

        if system_image is None:
            continue

        # Проверка, чтобы размеры изображений были совместимы для matchTemplate
        if system_image.shape[0] > search_area.shape[0] or system_image.shape[1] > search_area.shape[1]:
            print(f"Image {system_image_file} is too large for the search area, skipping.")
            continue

        result = cv2.matchTemplate(search_area, system_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.95:  # Порог совпадения, можно подстроить под нужные условия
            system_name = os.path.splitext(system_image_file)[0].capitalize()
#            print(f"Current system: {system_name} [{time.time() - solar_check_time:,.2f} sec]")
            break

    # Поиск изображений depot в screen_image
    depot_cnt = 0
    depot_images = ['gallente_depot_01.png', 'gallente_depot_02.png']
    for depot_image_file in depot_images:
        depot_image_path = os.path.join(icons_folder, depot_image_file)
        depot_image = cv2.imread(depot_image_path, cv2.IMREAD_GRAYSCALE)

        if depot_image is None:
            continue

        result = cv2.matchTemplate(cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY), depot_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        while max_val > 0.95:  # Порог совпадения, можно подстроить под нужные условия
            depot_cnt += 1
            # Затемняем найденную область, чтобы не учитывать её повторно
            top_left = max_loc
            bottom_right = (top_left[0] + depot_image.shape[1], top_left[1] + depot_image.shape[0])
            cv2.rectangle(screen_image, top_left, bottom_right, (0, 0, 0), -1)

            # Если найдено 3 Depot, то останавливаем проверку.
            if depot_cnt >= 3:
                break

            result = cv2.matchTemplate(cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY), depot_image, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

    print(f"System: {system_name}: {depot_cnt} [{time.time() - solar_check_time:,.2f} sec]")
    return system_name, depot_cnt


def warp_to_depot():
    """Функция для перемещения корабля к Depot"""
    depot_images = ['images/icons/gallente_depot_01.png', 'images/icons/gallente_depot_02.png']
    warp_icon_path = 'images/icons/warp_zero_icon.png'
    screen_image = get_screenshot()

    found_depot = False
    for depot_image_file in depot_images:
        depot_image = cv2.imread(depot_image_file)
        result = cv2.matchTemplate(screen_image, depot_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.95:
            found_depot = True
            top_left = max_loc

    if found_depot:
        pyautogui.moveTo(top_left[0] + depot_image.shape[1] // 2, top_left[1] + depot_image.shape[0] // 2)
        time.sleep(0.1)
        pyautogui.click()

        screen_image = get_screenshot()
        warp_icon = cv2.imread(warp_icon_path)
        result = cv2.matchTemplate(screen_image, warp_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.95:
            print(f"Sleep 5 sec")
            time.sleep(5)
            top_left = max_loc
            pyautogui.moveTo(top_left[0] + warp_icon.shape[1] // 2, top_left[1] + warp_icon.shape[0] // 2)
            time.sleep(0.1)
            pyautogui.click()
            print(f"Warp to Depot")
            return True
    return False



def warp_to_next_system():
    """Функция для перемещения в следующую солнечную систему"""
    gate_icon_path = 'images/icons/gate_yellow_icon.png'
    warp_to_gate_icon_path = 'images/icons/warp_to_gate.png'
    screen_image = get_screenshot()

    # Ищем иконку ворот
    gate_icon = cv2.imread(gate_icon_path)
    result = cv2.matchTemplate(screen_image, gate_icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.95:
        top_left = max_loc
        pyautogui.moveTo(top_left[0] + gate_icon.shape[1] // 2, top_left[1] + gate_icon.shape[0] // 2)
        time.sleep(0.1)
        pyautogui.click()

        screen_image = get_screenshot()
        warp_to_gate_icon = cv2.imread(warp_to_gate_icon_path)
        result = cv2.matchTemplate(screen_image, warp_to_gate_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.95:
            top_left = max_loc
            pyautogui.moveTo(top_left[0] + warp_to_gate_icon.shape[1] // 2, top_left[1] + warp_to_gate_icon.shape[0] // 2)
            time.sleep(0.1)
            pyautogui.click()
            print("Warp to next system")
            return True
    return False


def check_warping_status():
    """Функция для проверки состояния корабля (в варпе или нет)"""
    warping_icon_path = 'images/icons/warping.png'

    while True:
        screen_image = get_screenshot()
        warping_icon = cv2.imread(warping_icon_path)
        result = cv2.matchTemplate(screen_image, warping_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.95:
            print("Ship is still warping, waiting...")
            time.sleep(5)
        else:
            print("Ship has exited warp")
            break


def lock_on_depot():
    """Функция для поиска объекта депо и выполнения лока цели"""
    depot_icon_path = 'images/icons/depot_icon.png'
    screen_image = get_screenshot()

    depot_icon = cv2.imread(depot_icon_path)
    result = cv2.matchTemplate(screen_image, depot_icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.95:
        top_left = max_loc
        pyautogui.moveTo(top_left[0] + depot_icon.shape[1] // 2, top_left[1] + depot_icon.shape[0] // 2)
        time.sleep(0.1)
        pyautogui.keyDown('ctrl')
        pyautogui.click()
        pyautogui.keyUp('ctrl')
        print("Locked on depot")
        time.sleep(3)
        pyautogui.press('f1')
        print("Pressed F1")
        return True
    else:
        print("Depot icon not found")
        return False


# Пример использования:
time.sleep(3)

# Делаем скриншот экрана
screen_image = get_screenshot()

# Получаем название системы и количество Depot
system_name, depot_cnt = get_solar_system_and_depot_count(screen_image)

# Проверяем и перемещаемся к депо. Если депо в системе нет, тогда переходим в следующую систему.
if depot_cnt > 0:
    warp_to_depot()
    check_warping_status()
    lock_on_depot()
else:
    warp_to_next_system()
    check_warping_status()
