from tqdm import tqdm
import time

def sleep_progressbar(seconds):
    """Функция, которая показывает прогресс бар ожидания"""
    with tqdm(total=seconds, desc="Sleep", ncols=100, colour='green') as pbar:
        for _ in range(seconds):
            time.sleep(1)
            pbar.update(1)

# Пример использования
if __name__ == "__main__":
    sleep_progressbar(seconds=10)
