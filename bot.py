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
from find_board import get_start_position


position_board = get_start_position()

BOARD_SIZE = position_board[2]-4
DARK_SQUARE_THRESHOLD = 160
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+3
BOARD_LEFT_COORD = position_board[0]+2

CONFIDENCE = 0.99 # Уверенность определения фигуры
DETECTION_NOICE_THRESHOLD = 8 
PIECES_PATH = './images/figures/'

# players
WHITE = 0
BLACK = 1

# side to move
side_to_move = 0

# read argv if available
try:
    if sys.argv[1] == 'black': side_to_move = BLACK
except:
    print('usage: "chessbot.py white" or "chessbot.py black"')
    sys.exit(0)

# square to coords
square_to_coords = []

# array to convert board square indices to coordinates (black)
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

# locate piece on image
def locate_piece(screenshot, piece_location):
    # loop over pieces
    for index in range(len(piece_location)):
        piece = piece_location[index]
        
        # draw rectangle around recognized piece
        cv2.rectangle(screenshot, (piece.left, piece.top), (piece.left + piece.width, piece.top + piece.height), (0, 0, 255), 2)
    
    # display image
    cv2.imshow('Screenshot', screenshot)
    cv2.waitKey(0)

# Получение положения фигур
def recognize_position():
    piece_locations = {
        # b = black, w = white
        'b_rook_w': [],
        'b_horse_b': [],
        'b_bishop_w': [],
        'b_queen_b': [],
        'b_king_w': [],
        'b_bishop_b': [],
        'b_horse_w': [],
        'b_rook_b': [],
        'b_pawn_b': [],

        'w_pawn_w': [],
        'w_rook_b': [],
        'w_horse_w': [],
        'w_bishop_b': [],
        'w_queen_w': [],
        'w_king_b': [],
        'w_bishop_w': [],
        'w_horse_b': [],
        'w_rook_w': []
    }

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    
    # Переберает имена фигур
    # for piece in piece_names.keys():
    #     print(piece)
    #     PIECES_PATH + piece + '.png'
    
            


            
            # Отображает сообщение в консоль о найденой фигуре
            # piece_locations[piece].append(location)
            # print('detecting:', piece, location)
            
    return screenshot, piece_locations

# конвертирукт координаты фигур в FEN
def locations_to_fen(piece_locations):
    # FEN string
    fen = ''
    
    # board top left corner coords
    x = BOARD_LEFT_COORD
    y = BOARD_TOP_COORD
    
    # loop over board rows
    for row in range(8):
        # empty square counter
        empty = 0
            
        # loop over board columns
        for col in range(8):
            # init square
            square = row * 8 + col
            
            # piece detection
            is_piece = ()
            
            # loop over piece types
            for piece_type in piece_locations.keys():
                # loop over pieces
                for piece in piece_locations[piece_type]:
                    if abs(piece.left - x) < DETECTION_NOICE_THRESHOLD and \
                       abs(piece.top - y) < DETECTION_NOICE_THRESHOLD:
                        if empty:
                            fen += str(empty)
                            empty = 0

                        print(piece_names[piece_type])
                        fen += piece_names[piece_type]
                        is_piece = (square, piece_names[piece_type])

            
            if not len(is_piece):
                empty += 1
            
            # increment x coord by cell size
            x += CELL_SIZE
        
        if empty: fen += str(empty)
        if row < 7: fen += '/'
        
        # restore x coord, increment y coordinate by cell size
        x = BOARD_LEFT_COORD
        y += CELL_SIZE
    
    # add side to move to fen
    fen += ' ' + 'b' if side_to_move else ' w'
    
    # add placeholders (NO EN PASSANT AND CASTLING are static placeholders)
    fen += ' KQkq - 0 1'
    
    # return FEN string
    return fen
            
# находит лучший ход
def search(fen):
    print(fen)

    board = chess.Board(fen=fen)
    print(board)
    exit()

    # load Stockfish engine
    engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/Stockfish/stockfish.exe")
    # load BBC engine
    #engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/bbc/bbc.exe")
     # load Xiphos engine
    #engine = chess.engine.SimpleEngine.popen_uci("./chess_engines/xiphos/xiphos.exe")
    


    # get best move
    best_move = str(engine.play(board, chess.engine.Limit(time=3)).move)
    
    print(best_move)

    # close engine
    engine.quit()

    # search for the best move
    return best_move


################################    
#
#        Init coordinates
#
################################

# board top left corner coords
x = BOARD_LEFT_COORD
y = BOARD_TOP_COORD

# loop over board rows
for row in range(8):
    # loop over board columns
    for col in range(8):
        # init square
        square = row * 8 + col
        
        # associate square with square center coordinates
        square_to_coords.append((int(x + CELL_SIZE / 2), int(y + CELL_SIZE / 2)))

        # increment x coord by cell size
        x += CELL_SIZE
    
    # restore x coord, increment y coordinate by cell size
    x = BOARD_LEFT_COORD
    y += CELL_SIZE

################################    
#
#          Main driver
#
################################

while True:
    try:
        # locate pieces
        screenshot, piece_locations = recognize_position()

        # convert piece image coordinates to FEN string
        fen = locations_to_fen(piece_locations)

        best_move = search(fen)
        print('Best move:', best_move)

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











