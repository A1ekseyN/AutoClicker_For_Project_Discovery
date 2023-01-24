def global_timer_sec_to_minutes(x):
    # Функция для перерасчёта секунд в минуты.
    if x <= 60:
        return f'{round(x)} sec.'
    elif x > 60:
        minutes = x // 60
        sec = x % 60
        return f'{round(minutes)} minutes {round(sec)} sec.'
    elif x > 3600:
        hrs = round(x // 3600)
        minutes = round((x % 3600) / 60)
        return f'{hrs} hours {minutes} minutes.'
