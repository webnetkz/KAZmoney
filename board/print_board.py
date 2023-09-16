import chess

def print_board(fen):
    board = chess.Board(fen=fen)
    xBoard = str(board)

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
    return xBoard