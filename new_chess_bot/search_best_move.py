import chess
import chess.engine

def search_best_move(fen_position):
    board = chess.Board(fen_position) 
    engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")
    best_move = str(engine.play(board, chess.engine.Limit(time=0.3)).move)
    
    engine.quit()

    return best_move