#  Получение всех фигур со стартовой позиции

import cv2
import pyautogui as pg
import numpy as np

#from find_board import get_start_position

#position_board = get_start_position()
position_of_figures = 0



BOARD_SIZE = 832
BOARD_TOP_COORD = 172
BOARD_LEFT_COORD = 512
CELL_SIZE = int(BOARD_SIZE / 8)
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD


piece_names = {
    # b = black, w = white
    '0': 'b_rook',
    '1': 'b_horse',
    '2': 'b_bishop',
    '3': 'b_queen',
    '4': 'b_king',
    '5': 'b_pawn',

    '6': 'w_pawn',    
    '7': 'w_rook',
    '8': 'w_horse',
    '9': 'w_bishop',
    '10': 'w_queen',
    '11': 'w_king',
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
        if row in [0, 1, 6, 7]:
            # Пропускает пешки
            if row == 1 and col > 0: continue
            if row == 6 and col > 0: continue
            # Пропускает фигуры
            if row == 0 and col > 4: continue
            if row == 7 and col > 4: continue
                  
            # Получает изображение фигуры
            piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]

            bg_color = piece_image[0:3, 0:3]
            # cv2.imshow("x", bg_color)
            # cv2.waitKey(0)

            # cv2.imshow('scr', piece_image)
            # cv2.waitKey(0)

            piece_image = remove_color_from_image(bg_color, piece_image)
            # cv2.imshow('scr', x)
            # cv2.waitKey(0)
            # exit()
                  
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

