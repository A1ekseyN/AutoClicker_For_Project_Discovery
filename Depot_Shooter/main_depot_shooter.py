import time
import pyautogui
import cv2
import os
import numpy as np
from tqdm import tqdm


db = []
start_time = time.time()


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

    print(f"\nSystem: {system_name}: {depot_cnt} [{time.time() - solar_check_time:,.2f} sec]")
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
            time.sleep(0.1)
            top_left = max_loc
            pyautogui.moveTo(top_left[0] + warp_icon.shape[1] // 2, top_left[1] + warp_icon.shape[0] // 2)
            time.sleep(0.1)
            pyautogui.click()
            print(f"Warp to Depot")
            time.sleep(0.3)
            pyautogui.move(-12, -22)  # Перемещение курсора на 25 пикселей вверх
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
    else:
        warp_in_dock()
#        return False


def warp_in_dock():
    """Функция для варпа на док (желтый или белый)"""
    dock_yellow_icon_path = 'images/icons/dock_yellow.png'
    dock_white_icon_path = 'images/icons/dock_white.png'
    dock_icon_path = 'images/icons/dock_icon.png'
    screen_image = get_screenshot()

    # Ищем иконку dock_yellow
    dock_yellow_icon = cv2.imread(dock_yellow_icon_path)
    result = cv2.matchTemplate(screen_image, dock_yellow_icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.95:
        top_left = max_loc
        pyautogui.moveTo(top_left[0] + dock_yellow_icon.shape[1] // 2, top_left[1] + dock_yellow_icon.shape[0] // 2)
        time.sleep(0.1)
        pyautogui.click()
        print("Dock at yellow icon")
    else:
        # Иконка dock_yellow не найдена, ищем иконку dock_white
        dock_white_icon = cv2.imread(dock_white_icon_path)
        result = cv2.matchTemplate(screen_image, dock_white_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.95:
            top_left = max_loc
            pyautogui.moveTo(top_left[0] + dock_white_icon.shape[1] // 2, top_left[1] + dock_white_icon.shape[0] // 2)
            time.sleep(0.1)
            pyautogui.click()
            print("Dock at white icon")
        else:
            print("No dock icons found")
            return False

    # После клика по иконке дока, ищем иконку dock_icon.png
    time.sleep(0.2)
    screen_image = get_screenshot()
    dock_icon = cv2.imread(dock_icon_path)
    result = cv2.matchTemplate(screen_image, dock_icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.95:
        top_left = max_loc
        pyautogui.moveTo(top_left[0] + dock_icon.shape[1] // 2, top_left[1] + dock_icon.shape[0] // 2)
        time.sleep(0.1)
        pyautogui.click()
        print("Route End.")
        time.sleep(3600)
        return True
    else:
        print("Dock icon not found after initial dock click")
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
            time.sleep(10)
        else:
            print("Ship has exited warp")
            break


def check_warping_to_next_gate():
    """Функция для проверки статуса корабля, при варпе на слеующие ворота (в варпе или нет)"""
    warping_icon_path = 'images/icons/warp_speed_zero.png'
    warping_icon = cv2.imread(warping_icon_path)

    # Проверку на загрузку картинки можно убрать, если картинка правильно загружается
    if warping_icon is None:
        print(f"Error: Unable to load image at {warping_icon_path}")
        return

    attempts = 0
    max_attempts = 100  # Максимальное количество попыток, чтобы избежать бесконечного цикла

    while attempts < max_attempts:
        screen_image = get_screenshot()
        result = cv2.matchTemplate(screen_image, warping_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.95:
            print("Ship has exited warp")
            break
        else:
            print("Ship is still warping, waiting...")
            time.sleep(10)
            attempts += 1

    if attempts == max_attempts:
        print("Warning: Reached maximum attempts to check warp status. Exiting the loop.")


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
        time.sleep(0.1)
        return True
    else:
        print("Depot icon not found")
        return False


def update_system_db(system_name, depot_cnt):
    """Function to update the system_db with system_name and depot_cnt."""
    global db

    # Check if the system_name already exists in system_db
    for system_info in db:
        if system_info['system_name'] == system_name:
            # Update depot count if the system already exists
            system_info['depot_cnt'] = depot_cnt
            return

    # If system_name is not found, add it to system_db
    db.append({'system_name': system_name, 'depot_cnt': depot_cnt})

    # Optionally, print or log the update
    print(f"System updated: {system_name}: {depot_cnt}")
    print(', '.join(f"{entry['system_name']}: {entry['depot_cnt']}" for entry in db))


def sleep_with_progress(seconds):
    """Функция задержки с визуализацией через tqdm."""
    for _ in tqdm(range(seconds), desc="Sleeping", ncols=100, colour="green"):
        time.sleep(1)


# Пример использования:
print(f"Start after 3 seconds")
time.sleep(3)

# Делаем скриншот экрана
while True:
    screen_image = get_screenshot()

    # Получаем название системы и количество Depot
    system_name, depot_cnt = get_solar_system_and_depot_count(screen_image)

    # Update system_db with current system info
    update_system_db(system_name, depot_cnt)

    # Проверяем и перемещаемся к депо. Если депо в системе нет, тогда переходим в следующую систему.
#    while depot_cnt > 0:
    # Проверка на количество Depot в системе.
    for _ in range(depot_cnt):
#    if depot_cnt > 0:
        depot_cnt -= 1
        warp_to_depot()
        print(f"Sleep 20 sec")
        sleep_with_progress(20)
#        time.sleep(20)
        check_warping_status()
        lock_on_depot()
        print(f"Depots: {depot_cnt}\n")

#    else:
    warp_to_next_system()
    print(f"Sleep 45 sec.\n")
    sleep_with_progress(45)
#    time.sleep(45)
    check_warping_to_next_gate()
