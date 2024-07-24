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
def find_image(screenshot, template_path, threshold=0.9):
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


def move_mouse_up_left():
    """Функция для перемещения курсора чуть выше и левее"""
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x - 20, current_y - 23)


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
            time.sleep(0.2)

            # Перемещаем мышку на иконку врага и нажимаем левую кнопку мышки
            click_location(location)

            print("Враг найден, атакован и 'f1' нажата.")

            # Делаем еще один скриншот для поиска иконки орбиты
            screenshot = capture_screen()
#            orbit_icon_path = "images/orbit.png"
            keep_range_icon = "images/keep_range.png"
            location = find_image(screenshot, keep_range_icon)
            if location:
                click_location(location)
                print("Иконка держать дистанцию найдена и нажата.")

                check_inside_beacon_status(enemy=True)
            else:
                print("Иконка держать дистанцию не найдена.")
            break
    else:
        print("Враги не найдены.")


# Функция для проверки статуса внутри маяка
def check_inside_beacon_status(enemy):
    npc_image = "images/npc_red_fight_frigate.png"
    enemy_images = ["images/npc_red_cruiser.png", "images/npc_red_destroyer_1.png", "images/npc_red_frigate.png",
                    "images/npc_red_battle_cruiser.png"]
    beacon_icon = "images/beacon_circle.png"
    keep_range_icon = "images/keep_range.png"

    while True:
        time.sleep(5)
        screenshot = capture_screen()
        npc_location = find_image(screenshot, npc_image)
        beacon_move = True

        if npc_location:
            print("Мы наносим урон по NPC.")
        else:
            if enemy:
                print("В космосе нет NPC, с которыми мы сражаемся. Ждем нового противника.")
                enemy = False

                # Если закончился бой, тогда нажимаем Keep Range Beacon
                if beacon_move:
                    screenshot = capture_screen()
                    beacon_location = find_image(screenshot, beacon_icon)
                    if beacon_location:
                        click_location(beacon_location)
                        time.sleep(0.1)

                        # Находим кнопку Keep Range и нажимаем на нее
                        screenshot = capture_screen()
                        keep_range_icon_location = find_image(screenshot, keep_range_icon)
                        if keep_range_icon_location:
                            click_location(keep_range_icon_location)
                            print(f"Keep Range")
                        else:
                            print("Иконка держать дистанцию не найдена.")


def find_beacon_and_warp():
    """Функция для поиска маяка и варпа на маяк"""
    beacon_images = [
#        "images/gallente_mid_flt_1.png",
#        "images/gallente_mid_pro_1.png", "images/gallente_big_flt_5.png", "images/gallente_small_flt_5.png",
        "images/gallente_scout_flt.png",
    ]
    warp_icon_path = "images/warp_zero_icon.png"

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
            time.sleep(0.1)

            move_mouse_up_left()
            #            current_x, current_y = pyautogui.position()
            #            pyautogui.moveTo(current_x - 20, current_y - 23)

            sleep_progressbar(30)

        else:
            print("Иконка варпа не найдена.")
    else:
        print("Маяк не найден. Выполнение другой логики.")



def warp_inside_beacon():
    """Функция варпа внутрь маяка"""
    warp_in_beacon_path = "images/warp_in_beacon.png"
    jump_icon_path = "images/jump.png"


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
        move_mouse_up_left()

        # Ждем 45 секунд для прыжка
        print(f"Sleep 21")
        sleep_progressbar(21)

        return True
    else:
        print("Иконка прыжка не найдена.")
        return False


# Функция для поиска картинки из списка и выполнения действий
def test_find_and_act_on_enemy():
    # Делаем новый скриншот
    enemy_images = ["images/npc_red_frigate.png"]

    screenshot = capture_screen()

    # Поиск врагов
    for enemy in enemy_images:
        location = find_image(screenshot, enemy)
        if location:
            # Нажимаем 'f1'
            pyautogui.press('f1')

            # Ждем 0.1 секунды
            time.sleep(0.1)

            # Перемещаем мышку на иконку врага и нажимаем левую кнопку мышки
            x, y = location[1][0], location[0][0]  # координаты первой найденной точки
            pyautogui.moveTo(x, y)
            pyautogui.click()

            print(f"Враг {enemy} найден, атакован и 'f1' нажата.")
            return True  # Прерываем цикл после нахождения и выполнения действий
    return False  # Возвращаем False, если враги не найдены


# Основная функция для выполнения задачи
def main():
    find_beacon_and_warp()
    inside_beacon_status = warp_inside_beacon()

    if inside_beacon_status:
        # Логика поиска врагов внутри маяка
        kill_npc_logic()



# Запуск основного кода
if __name__ == "__main__":
#    check_inside_beacon_status(True)

    print("Beacon Roller. Sleep 3 sec")
    time.sleep(3)
    main()

#check_inside_beacon_status(True)

"""""""""
print("Start Testing")
time.sleep(3)
while True:
    test_find_and_act_on_enemy()
    move_mouse_up_left()
    print(f"Sleep 10 sec")
    time.sleep(10)
"""""