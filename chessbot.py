#####################################
# Шахматный бот, с возможностью выбора
# шахматного движка.
# For Windows
#####################################

import sys
import cv2
import numpy as np
import pyautogui as pg
import chess
import chess.engine
import time

# Получение стартовой позиции и ширины шахматной доски
from find_board import get_start_position
position_board = get_start_position()

# Константы для работы бота
BOARD_SIZE = position_board[2]-4
DARK_SQUARE_THRESHOLD = 160
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+4
BOARD_LEFT_COORD = position_board[0]+3

CONFIDENCE = 0.99 # Уверенность определения фигуры
DETECTION_NOICE_THRESHOLD = 8 
PIECES_PATH = './images/figures/'

# Игрок
WHITE = 0
BLACK = 1

side_to_move = 0

# Выбор игры за белых или черных
try:
    if sys.argv[1] == 'black': side_to_move = BLACK
except:
    print('Используй: "chessbot.py white" или "chessbot.py black"')
    sys.exit(0)

# Содершим координаты квадратов
square_to_coords = []

get_square = [
    'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
];
  
piece_names = {
    'b_rook_w': 'r',
    'b_horse_b': 'n',
    'b_bishop_w': 'b',
    'b_queen_b': 'q',
    'b_king_w': 'k',
    'b_queen_w': 'q',
    'b_king_b': 'k',
    'b_bishop_b': 'b',
    'b_horse_w': 'n',
    'b_rook_b': 'r',
    'b_pawn_b': 'p',
    # 'b_pawn_w': 'p',

    'w_pawn_b': 'P',
    'w_pawn_w': 'P',
    'w_rook_b': 'R',
    'w_horse_w': 'N',
    'w_bishop_b': 'B',
    'w_queen_w': 'Q',
    'w_king_b': 'K',
    'w_queen_b': 'Q',
    'w_king_w': 'K',
    'w_bishop_w': 'B',
    'w_horse_b': 'N',
    'w_rook_w': 'R'
}

# Получение положения фигур
def recognize_position():
    piece_locations = {
        # b = black, w = white
        'b_rook_w': [],
        'b_horse_b': [],
        'b_bishop_w': [],
        'b_queen_b': [],
        'b_king_w': [],
        'b_queen_w': [],
        'b_king_b': [],
        'b_bishop_b': [],
        'b_horse_w': [],
        'b_rook_b': [],
        'b_pawn_b': [],
        'b_pawn_w': [],


        'w_pawn_b': [],
        'w_pawn_w': [],
        'w_rook_b': [],
        'w_horse_w': [],
        'w_bishop_b': [],
        'w_queen_w': [],
        'w_king_b': [],
        'w_queen_b': [],
        'w_king_w': [],
        'w_bishop_w': [],
        'w_horse_b': [],
        'w_rook_w': []
    }

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)

    # Переберает имена фигур
    for piece in piece_names.keys():
        # Проверяет если фигура в сохраненных изображениях
        for location in pg.locateAllOnScreen(PIECES_PATH + piece + '.png', confidence=CONFIDENCE):
            # Не найдено совподение
            noise = False
            
            # Переберает клетки в поиске фигуры
            for position in piece_locations[piece]:
                # Обнаружение фигуры
                if abs(position.left - location.left) < DETECTION_NOICE_THRESHOLD and \
                   abs(position.top - location.top) < DETECTION_NOICE_THRESHOLD:
                    noise = True
                    break
            
            # Пропускаем
            if noise: continue
            
            # Отображает сообщение в консоль о найденой фигуре
            piece_locations[piece].append(location)
            print('detecting:', piece, location)
            
    return screenshot, piece_locations

# конвертирукт координаты фигур в FEN
def locations_to_fen(piece_locations):
    fen = ''
    
    x = BOARD_LEFT_COORD
    y = BOARD_TOP_COORD
    
    # Строки
    for row in range(8):
        empty = 0
    
        # Колонки
        for col in range(8):
            # Инициация квадрата
            square = row * 8 + col
            
            is_piece = ()
            
            # Перебераем типы фигур
            for piece_type in piece_locations.keys():
                # loop over pieces
                for piece in piece_locations[piece_type]:
                    if abs(piece.left - x) < DETECTION_NOICE_THRESHOLD and \
                       abs(piece.top - y) < DETECTION_NOICE_THRESHOLD:
                        if empty:
                            fen += str(empty)
                            empty = 0

                        fen += piece_names[piece_type]
                        is_piece = (square, piece_names[piece_type])

            
            if not len(is_piece):
                empty += 1
            
            # Переходим к следующей колонке
            x += CELL_SIZE
        
        if empty: fen += str(empty)
        if row < 7: fen += '/'
        
        # Переходим к следующей строке
        x = BOARD_LEFT_COORD
        y += CELL_SIZE
    
    # Добавляем FEN строку
    fen += ' ' + 'b' if side_to_move else ' w'
    fen += ' KQkq - 0 1' # Для уточнения рокировки
    
    return fen
            
# Находит лучший ход
def search(fen):
    print(fen)

    board = chess.Board(fen=fen)
    xBoard = str(board)
    #print(board)
    xBoard = xBoard.replace("P", "♙")
    xBoard = xBoard.replace("p", "♟")
    xBoard = xBoard.replace("R", "♖")
    xBoard = xBoard.replace("r", "♜")
    xBoard = xBoard.replace("B", "♗")
    xBoard = xBoard.replace("b", "♝")
    xBoard = xBoard.replace("N", "♘")
    xBoard = xBoard.replace("n", "♞")
    xBoard = xBoard.replace("K", "♔")
    xBoard = xBoard.replace("k", "♚")
    xBoard = xBoard.replace("Q", "♕")
    xBoard = xBoard.replace("q", "♛")

    print(xBoard)


    # Зпускаием Stockfish engine
    engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/Stockfish/stockfish.exe")
    # Зпускаием BBC engine
    #engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/bbc/bbc.exe")
    # Зпускаием Xiphos engine
    #engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/xiphos/xiphos.exe")
    
    # Получает лучший ход
    best_move = str(engine.play(board, chess.engine.Limit(time=1)).move)
    
    print(best_move)
    engine.quit()

    return best_move


x = BOARD_LEFT_COORD
y = BOARD_TOP_COORD

# Строки
for row in range(8):
    # Колонки
    for col in range(8):
        square = row * 8 + col
        square_to_coords.append((int(x + CELL_SIZE / 2), int(y + CELL_SIZE / 2)))

        # Следующия колонка
        x += CELL_SIZE
    
    # Следующая строка
    x = BOARD_LEFT_COORD
    y += CELL_SIZE


while True:
    try:
        # Определяет положение фигур
        screenshot, piece_locations = recognize_position()

        fen = locations_to_fen(piece_locations)

        best_move = search(fen)
        print('Возможно... это лучший ход:', best_move)

        # Получает позицию квадратов для хода
        from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
        to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

        # Совершает ход
        pg.moveTo(from_sq)
        pg.click()
        pg.moveTo(to_sq)
        pg.click()
        print(from_sq)
        pg.moveTo(500, 100)
        time.sleep(3)
    
    except: sys.exit(0)











