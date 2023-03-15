#  Получение всех фигур со стартовой позиции

import cv2
import pyautogui as pg
import numpy as np
from draw import draw_rect
import sys

from find_board import get_start_position
position_board = get_start_position()
position_of_figures = 0


BOARD_SIZE = position_board[2]-4
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+4
BOARD_LEFT_COORD = position_board[0]+3
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD

# Игрок
WHITE = 0
BLACK = 1

side_to_move = 0

# Выбор игры за белых или черных
try:
    if sys.argv[1] == 'b': side_to_move = BLACK
except:
    print('Используй: "find_king_queen.py w" или "find_king_queen.py b"')
    sys.exit(0)


if side_to_move == 0:
  piece_names = {
    # b = black, w = white
    '0': 'w_queen_b',
    '1': 'w_king_w',
  }
else:
  piece_names = {
    # b = black, w = white
    '0': 'b_queen_w',
    '1': 'b_king_b',
  }

# Получает изображение и обрабатывает его
pg.screenshot('screenshot.png')
screenshot = cv2.imread('screenshot.png')

# Код фигуры
piece_code = 0


# Строки
for row in range(8):
    # Колонки
    for col in range(8):
        # Перебераем строки с фигурами
        if row == 6:
            if col == 3 or col == 4:
              # Получает изображение фигуры
              piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]
              draw_rect(x,y,CELL_SIZE)      
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

