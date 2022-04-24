# AutoClicker for Project Discovery in Eve Online
# Version - 0.0.3a
# Работает ноутбуке, с персонажами: Allehandro, Anna de Amarr, Elise Jackson, Suzanne Jackson, Blondie Loo

# Omega clone - 200 заданий в день
# Alpha clone - 100 заданий в день (Нужно уточнить число)

# Tasks (Фичи):
# Дописать остановку выполнения скрипта
# Возможность по хоткею добавлять таски в задания
# GUI интерфейс (Не понятно или он сейчас нужен)
# Функционал, который запоминает время обнуления Project Discovery

# Идеи для бота:
# Авто-подскан каждые 3-5 секунд, по горячей кнопке.
# Добавить клик по кнопке перехода через гипер-врата. (Скорее всего активируется отдельно, через команду if)

# 1. Allehandro - приверно - 14.29 (21.03.2022)
# 1. Anna de Amarr - Нет 1.000.000 skill point
# 2. Elise Jackson - 2Do
# 2. Suzane Jackson - < 914k exp
# 3. Blondie Loo - 2Do

import time
import threading
import pynput
from pynput.mouse import Button, Controller

from datetime import timedelta

mouse = Controller()

#####################################
# !!! Start - стартовать нужно с главного окна Project Discovery.
# Там где показан счёт. То, есть по сути 1 проект дисковери нужно пройти.
#####################################

counter = input("Сколько циклов выполнить? ")
counter = int(counter)

# Characters: // Allehandor - 0 (???)   // Anna de Amarr --- // Elise Jackson - 66 // Suzane Jackson --- // Blondie Loo - 10
# timestamp:  //time = 14.48 (22) //       ---         // time = 13.29 (17)  // time = 15.55 (02)   //  time = 16.00 (22)

isk_for_task = (counter * 99000)

task_time_one = timedelta(minutes=0, seconds=12.356)
task_time_total = task_time_one * counter


print(f"Предположительный доход за {counter} заданий {isk_for_task:,.0f} isk.")
print(f"Время на выполнение задания: {task_time_total}.")

def timer_start():
    print("\nСтарт через 7 секунд.")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Старт!")

# Вызов функции таймера перед стартом. На данный момент таймер настроен на 7 секунд.
timer_start()

# Start timer
start_time = time.time()

mouse.position = (0, 0)
print("Corrent position: " + str(mouse.position))


##### Start Цикла While #####
# Цикл прохождения задания в Project Discovery.

def project_discovery(counter=counter):
    while counter > 0: # Счётчик цикла

        ##### Start Discovery Project #####
        time.sleep(1)
        mouse.position = (1248, 771)
        time.sleep(1)
        mouse.click(Button.left, 1)

        ##### First border #####
        time.sleep(2.4)
        mouse.position = (255, 277)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (257, 539)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (682, 535)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (666, 292)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (255, 277)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        ##### Second border #####
        time.sleep(0.3)
        mouse.position = (257, 550)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (260, 742)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (715, 738)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.3)
        mouse.position = (711, 549)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

        time.sleep(0.4)
        mouse.position = (257, 550)
        time.sleep(0.4)
        mouse.click(Button.left, 1)

        ##### Click to Procced button #####
        mouse.position = (1248, 771)
        time.sleep(1)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.click(Button.left, 1)

        # Конец цикла и одного задания Project Discovery
        print(f"Осталось {counter} циклов.")
        print("--- %s seconds ---" % (time.time() - start_time))

        counter -= 1

# Выполнение заданий Project Discovery.
project_discovery()


print("Конец выполнения программы.")
print("--- %s seconds ---" % (time.time() - start_time))


