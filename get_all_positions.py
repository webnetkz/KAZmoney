#  Получение всех фигур со стартовой позиции

import cv2
import pyautogui as pg
import numpy as np
from matches import find_matching_contours
import os


#from find_board import get_start_position

#position_board = get_start_position()
position_of_figures = 0



PIECES_PATH = './images/figures/'
BOARD_SIZE = 832
BOARD_TOP_COORD = 172
BOARD_LEFT_COORD = 512
CELL_SIZE = int(BOARD_SIZE / 8)
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD


piece_names = {
    # b = black, w = white
    'b_rook_w': 'r',
    'b_horse_b': 'n',
    'b_bishop_w': 'b',
    'b_queen_b': 'q',
    'b_king_w': 'k',
    'b_bishop_b': 'b',
    'b_horse_w': 'n',
    'b_rook_b': 'r',
    'b_pawn_b': 'p',

    'w_pawn_w': 'P',
    'w_rook_b': 'R',
    'w_horse_w': 'N',
    'w_bishop_b': 'B',
    'w_queen_w': 'Q',
    'w_king_b': 'K',
    'w_bishop_w': 'B',
    'w_horse_b': 'N',
    'w_rook_w': 'R'
}

def remove_color_from_image(bg_image, target_image):
    # Получаем фоновый цвет из первого изображения
    bg_color = np.array(cv2.mean(bg_image)[:3], dtype=np.uint8)

    # Извлекаем маску цвета, который нужно удалить из второго изображения
    mask = cv2.inRange(target_image, bg_color, bg_color)

    # Применяем маску на второе изображение, чтобы удалить цвет фона
    result = cv2.bitwise_and(target_image, target_image, mask=~mask)

    return result


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
        if row in [0, 1, 3, 4, 5, 6, 7]:
            # Получает изображение фигуры
            piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]
            bg_color = piece_image[0:3, 0:3]
            piece_image = remove_color_from_image(bg_color, piece_image)
            piece_image = cv2.cvtColor(piece_image, cv2.COLOR_BGR2GRAY)

            cv2.imwrite('tmp.png', piece_image)
            # cv2.waitKey(0)
            # 35
            # pawn w, bishop w-b
            # 20
            # pawn b, horse w
            # 19
            # horse b
            
            if find_matching_contours("tmp.png", PIECES_PATH+'b_king_w'+'.png'):
              print("b_bishop_b", piece_code)


            os.remove("tmp.png")
                  
            
            # Обновляет код фигуры
            piece_code += 1
          
        # Смещает итерацию на следующую клетку
        x += CELL_SIZE
      
    # Смещает итерацию на строку ниже
    x = BOARD_LEFT_COORD
    y += CELL_SIZE


cv2.destroyAllWindows()

