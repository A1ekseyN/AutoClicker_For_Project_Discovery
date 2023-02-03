import pyautogui
from datetime import datetime
from pictures import drop_box_png, dread_guristas_png, take_all_loot_png
from settings import dread_guristas_take_loot


def check_dread_guristas_loot():
    # Сбор лута с фракционника Dread Guristas
    if dread_guristas_take_loot:
        # Если в настройках стоит True, тогда работает.
        start_time = datetime.now().time()
        try:
            if pyautogui.locateOnScreen(dread_guristas_png, confidence=0.9):
                dread_guristas_loot = pyautogui.locateOnScreen(dread_guristas_png, confidence=0.9)
                pyautogui.moveTo(dread_guristas_loot)
        #        pyautogui.sleep(0.1)
                pyautogui.doubleClick()
                pyautogui.sleep(1)
                # Включение MWD
                pyautogui.press('1')
                pyautogui.sleep(1)
                pyautogui.press('1')
                if pyautogui.locateOnScreen(drop_box_png, confidence=0.9) and pyautogui.locateOnScreen(dread_guristas_png, confidence=0.9):
                    drop_box = pyautogui.locateOnScreen(drop_box_png, confidence=0.9)
                    pyautogui.moveTo(drop_box)
                    pyautogui.sleep(1)
                    pyautogui.click()

                    while not pyautogui.locateOnScreen(take_all_loot_png, confidence=0.9):
                        # Когда появляется кнопка забрать "Взять Все", забираем лут.
                        pyautogui.sleep(5)
                        continue
                    if pyautogui.locateOnScreen(take_all_loot_png, confidence=0.9):
                        take_loot = pyautogui.locateOnScreen(take_all_loot_png, confidence=0.9)
                        pyautogui.moveTo(take_loot, 1)
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print(f'-- Dread Guristas Take Loot.')
#                        print(f'Dread Guristas Take Loot: {round(datetime.now().timestamp() - start_time):,.2f} sec.')
        except:
            print('Error Dread Guristas take loot')

        print('Dread Guristas Check: {time_not_work}')
#        print(f'Dread Guristas Check: {round(datetime.now().timestamp() - start_time):,.2f} sec.')
