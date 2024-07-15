# pyinstaller --onefile --icon=icon.ico Project_Discovery/project_discovery.py
import time
import csv
import json
from datetime import datetime, timedelta
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from pynput import keyboard
import sys
import os
import threading


mouse = Controller()
version = '0.0.5d'

# Константы
#CSV_FILE = 'project_discovery_db.csv'
JSON_FILE = 'project_discovery_db.json'
MAX_ITERATIONS_OMEGA_TRUE = 200
MAX_ITERATIONS_OMEGA_FALSE = 100
RESET_HOURS = 24

# Глобальные переменные для управления состоянием выполнения скрипта
pause_flag = False
exit_flag = False


def load_data():
    """Загрузка данных из JSON-файла или инициализация по умолчанию, если файл не существует или поврежден."""
    if not os.path.exists(JSON_FILE):
        # Инициализация данных, если файл не существует
        return initialize_data()

    try:
        with open(JSON_FILE, mode='r') as file:
            data = json.load(file)
            # Преобразование строк 'start_time' в объекты datetime
            for char_data in data.values():
                if isinstance(char_data['start_time'], str):
                    char_data['start_time'] = datetime.strptime(char_data['start_time'], '%Y-%m-%d %H:%M:%S')
    except (json.JSONDecodeError, FileNotFoundError):
        # Если JSON-файл поврежден или не может быть декодирован, инициализируем данные
        print(f"JSON-файл '{JSON_FILE}' поврежден или не существует. Инициализация данных.")
        return initialize_data()

    return data

def initialize_data():
    """Инициализация данных значениями по умолчанию."""
    data = {
        'Allehandro': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True},
        'Anna de Amarr': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True},
        'Elise Jackson': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True},
        'Suzane Jackson': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True},
        'Lilf Moliko': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True},
        'Blondie Loo': {'iterations': MAX_ITERATIONS_OMEGA_TRUE, 'start_time': datetime.now(), 'omega': True}
    }
    save_data(data)
    return data


def save_data(data):
    """Сохранение данных в JSON-файл."""
    # Преобразование объектов datetime в строки для 'start_time'
    data_to_save = {}
    for char_name, char_data in data.items():
        data_to_save[char_name] = {
            'iterations': char_data['iterations'],
            'start_time': char_data['start_time'].strftime('%Y-%m-%d %H:%M:%S'),
            'omega': char_data['omega']
        }

    with open(JSON_FILE, mode='w') as file:
        json.dump(data_to_save, file, indent=4)


def counter_iteration(data, character):
    """Спрашиваем, сколько нужно сделать итераций."""
    global counter
    print(f"\nPause: 'F3'"
          f"\nContinue: 'F4'")
    try:
        counter = int(input(f"\nСколько циклов выполнить для {character}? (Осталось {data[character]['iterations']} итераций)\n>>> "))
        if counter > data[character]['iterations']:
            print(f"Ошибка: Максимальное количество итераций для {character} - {data[character]['iterations']}")
            return counter_iteration(data, character)
        return counter
    except ValueError:
        print('Пожалуйста, введите число.')
        return counter_iteration(data, character)


def timer_to_start(seconds=7):
    """Функция обратного отсчета перед стартом выполнения задания."""
    print(f"\nСтарт через {seconds} секунд.")
    for t in range(seconds, 0, -1):
        print(f"{t}")
        time.sleep(1)
    print("Старт!")


def on_press(key):
    global pause_flag, exit_flag
    try:
        if key == Key.f3:
            if not pause_flag:
                pause_flag = True
                print("\nPause. Enter 'F4' to continue.\n")
            else:
                pause_flag = False
                print("Скрипт продолжен.")
        elif key == Key.f4:
            if pause_flag:
                pause_flag = False
                print("\nContinue.")
        elif key == Key.esc:
            exit_flag = True
            print("Выход из скрипта.")
            return False
    except AttributeError:
        pass


def project_discovery(counter, isk_per_task, task_time_one, character, data, start_time):
    """Цикл прохождения задания в Project Discovery."""
    global pause_flag, exit_flag

    earned_isk = 0  # Инициализация переменной earned_isk

    # Начало отслеживания нажатий клавиш
    def key_listener():
        global exit_flag  # Используем global вместо nonlocal для exit_flag
        with Listener(on_press=on_press) as listener:
            listener.join()

    key_thread = threading.Thread(target=key_listener)
    key_thread.start()

    while counter > 0 and not exit_flag:
        if pause_flag:
            time.sleep(1)
            continue

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

        ##### Click to Proceed button #####
        mouse.position = (1248, 771)
        time.sleep(1)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.click(Button.left, 1)

        # Обновление заработанных ISK
        earned_isk += isk_per_task

        # Обновление оставшегося времени
        remaining_time = task_time_one.total_seconds() * (counter - 1)

        # Конец цикла и одного задания Project Discovery
        elapsed_time = time.time() - start_time
        print(f"Осталось: {counter - 1} циклов. "
              f"Заработано ISK: {earned_isk:,.0f} ISK. (Pause: F3)"
              f"\nВремя выполнения скрипта: {elapsed_time:,.2f} сек. "
              f"Оставшееся время: {remaining_time:.2f} секунд.\n")

        counter -= 1
        data[character]['iterations'] -= 1

    save_data(data)


def start_project_discovery(character):
    """Метод для запуска кликера Project Discovery."""
    data = load_data()

    # Проверяем, нужно ли сбросить итерации для выбранного персонажа
    if datetime.now() - data[character]['start_time'] >= timedelta(hours=RESET_HOURS):
        data[character]['iterations'] = MAX_ITERATIONS_OMEGA_TRUE if data[character]['omega'] else MAX_ITERATIONS_OMEGA_FALSE
        data[character]['start_time'] = datetime.now()

    iteration_counter = counter_iteration(data, character)  # Определяем число итераций

    isk_per_task = 99000
    isk_for_task = iteration_counter * isk_per_task
    task_time_one = timedelta(seconds=12.356)
    task_time_total = task_time_one * iteration_counter  # Изменение здесь

    # Форматирование времени в часах, минутах и секундах без миллисекунд
    task_time_total_str = str(task_time_total).split('.')[0]

    print(f"\nПредположительный доход за {iteration_counter} заданий {isk_for_task:,.0f} isk.")
    print(f"Время на выполнение заданий: {task_time_total_str}")

    timer_to_start()  # Запускаем таймер обратного отсчёта

    start_time = time.time()
    project_discovery(iteration_counter, isk_per_task, task_time_one, character, data, start_time)  # Запуск автокликера

    print("--- Конец выполнения программы. ---")
    print(f'Выполнено за: {time.time() - start_time:,.2f} сек.')
    save_data(data)  # Сохраняем данные после выполнения итераций


def repeat():
    """Повтор выполнения программы."""
    ask = input('\nПовторить ход выполнения программы? (Press any key) or (q or Q for exit).\n>>> ')
    if ask.lower() in ('q', 'й'):
        sys.exit()
    else:
        print()
        character = select_character()
        start_project_discovery(character)
        repeat()


def select_character():
    """Выбор персонажа пользователем."""
    data = load_data()
    print("Выберите персонажа:")
    for i, (name, info) in enumerate(data.items(), 1):
        if isinstance(info['start_time'], str):
            info['start_time'] = datetime.strptime(info['start_time'], '%Y-%m-%d %H:%M:%S')  # Преобразуем строку в datetime

        time_left = timedelta(hours=RESET_HOURS) - (datetime.now() - info['start_time'])
        iterations = info['iterations']
        if time_left.total_seconds() <= 0:
            iterations = MAX_ITERATIONS_OMEGA_TRUE if info['omega'] else MAX_ITERATIONS_OMEGA_FALSE
            time_left = "Updated"
        else:
            time_left = str(time_left).split(".")[0]  # Убираем микросекунды
        print(f"{i}. {name} - Iterations: {iterations}, Updated after: {time_left}")

    choice = input("\nВведите цифру: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(data):
            return list(data.keys())[choice - 1]
        else:
            print("Неверный выбор. Попробуйте снова.")
            return select_character()
    except ValueError:
        print("Неверный выбор. Попробуйте снова.")
        return select_character()


if __name__ == "__main__":
    print(f"Version: {version}\n")
    data = load_data()
    character = select_character()
    start_project_discovery(character)
    repeat()  # Повтор выполнения скрипта.
