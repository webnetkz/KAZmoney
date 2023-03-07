#  Получение всех фигур со стартовой позиции

# "k1q1r1b1/1n1p4/8/8/8/1N1P4/K1Q1R1B1/8 w - - 0 1"
# "k1q1r1b1/1n1p4/8/8/8/1N1P4/K1Q1R1B1/8 w KQkq - 0 1"

import cv2
import pyautogui as pg
from find_board import get_start_position

position_board = get_start_position()

BOARD_SIZE = position_board[2]-4
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+3
BOARD_LEFT_COORD = position_board[0]+2
y = BOARD_TOP_COORD
x = BOARD_LEFT_COORD
# BOARD_SIZE = 832
# BOARD_TOP_COORD = 172
# BOARD_LEFT_COORD = 512


piece_names = {
    # b = black, w = white
    '0': 'b_rook_w',
    '1': 'b_horse_b',
    '2': 'b_bishop_w',
    '3': 'b_queen_b',
    '4': 'b_king_w',
    '5': 'b_bishop_b',
    '6': 'b_horse_w',
    '7': 'b_rook_b',
    '8': 'b_pawn_b',
    '9': 'b_pawn_w',

    '10': 'w_pawn_w',
    '11': 'w_pawn_b',
    '12': 'w_rook_b',
    '13': 'w_horse_w',
    '14': 'w_bishop_b',
    '15': 'w_queen_w',
    '16': 'w_king_b',
    '17': 'w_bishop_w',
    '18': 'w_horse_b',
    '19': 'w_rook_w'
}

# Получает изображение и обрабатывает его
pg.screenshot('screenshot.png')
screenshot = cv2.imread('screenshot.png')
screenshot_grayscale = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Код фигуры
piece_code = 0

# Строки
for row in range(8):
    # Колонки
    for col in range(8):
        # Перебераем строки с фигурами
        if row in [0, 1, 6, 7]:
            # Пропускает клетки с пешками
            if row == 1 and col > 1: continue
            if row == 6 and col > 1: continue
                
            # Получает изображение фигуры
            piece_image = screenshot[y:y + CELL_SIZE, x: x + CELL_SIZE]

                
            # cv2.imshow('scr', piece_image)
            # cv2.waitKey(0)
                
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

