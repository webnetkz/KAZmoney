import pyautogui

def get_mouse_position():
    # Получите текущие координаты указателя мыши
    x, y = pyautogui.position()
    return x, y

# Пример использования:
while True:
    x, y = get_mouse_position()
    print(f"Текущие координаты мыши: X={x}, Y={y}")
