# AutoClicker for Project Discovery in Eve Online
# auto-py-to-exe
# Version - 0.0.4b


import time
from pynput.mouse import Button, Controller
from datetime import datetime, timedelta


mouse = Controller()


def counter_iteration():
    # Запрос на кол-во циклов.
    global counter
    try:
        counter = int(input("\nСколько циклов выполнить?\n>>> "))
    except:
        print('Лучше ввести число.')
        counter_iteration()

counter_iteration()


isk_for_task = (counter * 99000)
task_time_one = timedelta(minutes=0, seconds=12.356)
task_time_total = task_time_one * counter

print(f"\nПредположительный доход за {counter} заданий {isk_for_task:,.0f} isk.")
print(f"Время на выполнение задания: {task_time_total}.")


def timer_start():
    # Функция обратного отчета перед стартом выполнения задания.
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

timer_start()

start_time = time.time()

mouse.position = (0, 0)
print("Corrent position: " + str(mouse.position))


def project_discovery(counter=counter):
    # Цикл прохождения задания в Project Discovery.
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
        print(f"\nОсталось: {counter} циклов.")
        print(f'Время выполнения скрипта: {time.time() - start_time:,.2f} сек.')
        print(f'Осталось времени: {task_time_total - timedelta(seconds=12.356)}.')

        counter -= 1

project_discovery()


print("\n--- Конец выполнения программы. ---")
print(f'Выполнено за: {time.time() - start_time:,.2f} сек.')


def repeat():
    # Повтор выполнения программы.
    ask = input('\nПовторить ход выполнения программы? (Press any key) or (q or Q for exit).\n>>> ')
    if ask == 'й' or ask == 'q' or ask == 'Q' or ask == 'Й':
        pass
    else:
        counter_iteration()
        timer_start()
        project_discovery(counter)
        repeat()

repeat()        # Повтор выполнения скрипта.
