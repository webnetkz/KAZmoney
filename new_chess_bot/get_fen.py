import chess

def get_fen(positions):
    board = chess.Board()

    # Функция для преобразования текстового представления фигур в символы шахматных фигур
    def piece_to_symbol(piece):
        if "pawn" in piece:
            return "P" if "white" in piece else "p"
        if "knight" in piece:
            return "N" if "white" in piece else "n"
        if "bishop" in piece:
            return "B" if "white" in piece else "b"
        if "rook" in piece:
            return "R" if "white" in piece else "r"
        if "queen" in piece:
            return "Q" if "white" in piece else "q"
        if "king" in piece:
            return "K" if "white" in piece else "k"
        return " "

    # Установите фигуры на доске на основе списка позиций
    for square, piece in positions.items():
        if piece_to_symbol(piece) != " ":
            board.set_piece_at(chess.parse_square(square), chess.Piece.from_symbol(piece_to_symbol(piece)))

    # Получите FEN позицию
    fen_position = board.fen()
    return fen_position
