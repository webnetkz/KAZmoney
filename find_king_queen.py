#  Получение всех фигур со стартовой позиции

import cv2
import pyautogui as pg
import numpy as np

from find_board import get_start_position
position_board = get_start_position()
position_of_figures = 0


BOARD_SIZE = position_board[2]-4
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+4
BOARD_LEFT_COORD = position_board[0]+3
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD


piece_names = {
  # b = black, w = white
  '0': 'b_king_b',
  '1': 'b_queen_w',
  '2': 'w_king_w',
  '3': 'w_queen_b',
}


# Получает изображение и обрабатывает его
pg.screenshot('screenshot.png')
screenshot = cv2.imread('screenshot.png')
#screenshot_grayscale = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Код фигуры
piece_code = 0

# Строки
for row in range(8):
    # Колонки
    for col in range(8):
        # Перебераем строки с фигурами
        if row == 6:
            # Пропускает клетки с пешками
            if row == 1 and col > 2: continue
            if row == 6 and col > 2: continue

            # Получает изображение фигуры
            piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]
                  
            # Сохраняет изображения
            cv2.imwrite('./images/figures/' + piece_names[str(piece_code)] + '.png', piece_image)
                  
            # Обновляет код фигуры
            piece_code += 1
          
        # Смещает итерацию на следующую клетку
        x += CELL_SIZE
      
    # Смещает итерацию на строку ниже
    x = BOARD_LEFT_COORD
    y += CELL_SIZE


cv2.destroyAllWindows()

