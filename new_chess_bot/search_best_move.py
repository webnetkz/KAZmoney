import chess
import chess.engine

def search_best_move(fen_position):
    board = chess.Board(fen_position) 
    engine = chess.engine.SimpleEngine.popen_uci("/mnt/c/Users/dbqqb/onchessbot/new_chess_bot/stockfish.exe")
    best_move = str(engine.play(board, chess.engine.Limit(time=0.4)).move)
    
    engine.quit()

    return best_move