def global_timer_sec_to_minutes(x):
    # Функция для перерасчёта секунд в минуты.
    if x <= 60:
        return f'{round(x)} sec.'
    elif x > 60:
        minutes = x // 60
        sec = x % 60
        return f'{round(minutes)} minutes {round(sec)} sec.'
