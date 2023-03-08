#####################################
# Шахматный бот, с возможностью выбора
# шахматного движка.
# For Windows
#####################################
import lichess.api
from lichess.format import PYCHESS
import sys
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


def getFen():
  game = lichess.api.game('fUUGwWWe', format=PYCHESS)
  board = game.end().board()
  fen = board.fen()
  return fen

# находит лучший ход
def search(fen):
    # create chess board instance and set position from FEN string
    print('Searching best move for this position:')
    print(fen)
    board = chess.Board(fen=fen)
    print(board)

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
        fen = getFen()

        best_move = search(fen)
        print('Best move:', best_move)

        # extract source and destination square coordinates
        from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
        to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

        # make move on board
        pg.moveTo(from_sq)
        pg.click()
        pg.moveTo(to_sq)
        pg.click()
        print(from_sq)
        pg.moveTo(500, 100)
        
        # wait for 3 seconds
        time.sleep(3)
    
    except: sys.exit(0)