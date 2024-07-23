import cv2
import numpy as np
import pyautogui
import time

from time_functions import sleep_progressbar



# Функция для снятия скриншота экрана
def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot


# Функция для поиска изображения на экране
def find_image(screenshot, template_path, threshold=0.8):
    template = cv2.imread(template_path)
    if template is None:
        print(f"Ошибка: не удалось загрузить изображение {template_path}")
        return None
    if template.shape[2] == 4:  # Если изображение имеет альфа-канал
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        return loc
    return None


# Функция для поиска маяков на экране
def find_beacon(screenshot, beacon_images):
    for beacon in beacon_images:
        location = find_image(screenshot, beacon)
        if location:
            return location
    return None


# Функция для перемещения курсора и клика
def click_location(location):
    x, y = location[1][0], location[0][0]  # координаты первой найденной точки
    pyautogui.moveTo(x, y)
    pyautogui.click()


# Функция для выполнения логики прыжка
def kill_npc_logic():
    # Делаем новый скриншот
    screenshot = capture_screen()

    # Переменная для хранения информации о врагах
    enemy_images = ["images/npc_red_cruiser.png", "images/npc_red_destroyer_1.png", "images/npc_red_frigate.png",
                    "images/npc_red_battle_cruiser.png"]

    # Поиск врагов
    for enemy in enemy_images:
        location = find_image(screenshot, enemy)
        if location:
            # Нажимаем 'f1'
            pyautogui.press('f1')

            # Ждем 0.1 секунды
            time.sleep(0.1)

            # Перемещаем мышку на иконку врага и нажимаем левую кнопку мышки
            click_location(location)

            print("Враг найден, атакован и 'f1' нажата.")

            # Делаем еще один скриншот для поиска иконки орбиты
            screenshot = capture_screen()
            orbit_icon_path = "images/orbit.png"
            location = find_image(screenshot, orbit_icon_path)
            if location:
                click_location(location)
                print("Иконка орбиты найдена и нажата.")
            else:
                print("Иконка орбиты не найдена.")
            break
    else:
        print("Враги не найдены.")


# Основная функция для выполнения задачи
def main():
    beacon_images = [
#        "images/gallente_mid_pro_1.png", "images/gallente_big_flt_5.png", "images/gallente_small_flt_5.png",
        "images/gallente_scout_flt.png",
    ]
    warp_icon_path = "images/warp_zero_icon.png"
    warp_in_beacon_path = "images/warp_in_beacon.png"
    jump_icon_path = "images/jump.png"

    screenshot = capture_screen()
    location = find_beacon(screenshot, beacon_images)
    if location:
        click_location(location)
        print(f"Маяк найден и выбран.")

        # Делаем новый скриншот после выбора маяка
        time.sleep(2)  # Даем время для загрузки экрана
        screenshot = capture_screen()
        location = find_image(screenshot, warp_icon_path)
        if location:
            click_location(location)
            print("Иконка варпа найдена и нажата.")
            print(f"Sleep 30 sec")

            sleep_progressbar(30)
            ###

            # Ищем кнопку разгонных ворот
            # Делаем новый скриншот после прыжка
            screenshot = capture_screen()
            location = find_image(screenshot, warp_in_beacon_path)
            if location:
                click_location(location)
                print("Иконка варпа в маяк найдена и нажата.")
            else:
                print("Иконка варпа в маяк не найдена.")

            # Ждем 30 секунд после входа в маяк
            time.sleep(0.1)

            # Делаем новый скриншот после нажатия варпа
            screenshot = capture_screen()
            location = find_image(screenshot, jump_icon_path)
            if location:
                click_location(location)
                print("Иконка прыжка найдена и нажата.")
                time.sleep(0.1)

                # Перемещаем курсор на 23 пикселя вверх и 20 пикселей влево
                current_x, current_y = pyautogui.position()
                pyautogui.moveTo(current_x - 20, current_y - 23)

                # Ждем 45 секунд для прыжка
                print(f"Sleep 21")
                sleep_progressbar(21)

                # Выполняем логику прыжка и поиска врагов
                kill_npc_logic()
            else:
                print("Иконка прыжка не найдена.")
        else:
            print("Иконка варпа не найдена.")
    else:
        print("Маяк не найден. Выполнение другой логики.")


# Запуск основного кода
if __name__ == "__main__":
    print("Beacon Roller. Sleep 3 sec")
    time.sleep(3)
    main()
