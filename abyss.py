def abyss_go_to_gate():
    abyss_gate_button = pyautogui.locateOnScreen(abyss_gate_png, confidence=0.9)
    pyautogui.moveTo(abyss_gate_button)
    pyautogui.sleep(0.2)
    pyautogui.click


def abyss_lock_container():
    abyss_container_button = pyautogui.locateOnScreen(abyss_container_png, confidence=0.8)
    pyautogui.click(abyss_container_button)

