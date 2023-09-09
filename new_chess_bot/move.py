import pyautogui

def draw_chess_board(x, y, width, height, target_square):
    num_rows = 8
    num_cols = 8

    left = x
    top = y
    right = x + width
    bottom = y + height

    # Размер одной клетки
    cell_width = width / num_cols
    cell_height = height / num_rows

    target_col, target_row = ord(target_square[0]) - ord('a'), int(target_square[1]) - 1
    # Инвертируем координату y для согласования с системой координат PyAutoGUI
    target_x = left + (target_col + 0.5) * cell_width
    target_y = bottom - (target_row + 0.5) * cell_height
    
    # Переместите указатель мыши к целевой клетке
    pyautogui.moveTo(target_x, target_y, duration=0.5)

# Пример использования:
x = 570
y = 208
width = 701
height = 701

draw_chess_board(x, y, width, height, 'e1')
