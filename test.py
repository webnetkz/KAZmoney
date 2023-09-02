from new_chess_bot.get_position import get_position
from new_chess_bot.get_fen import get_fen
from new_chess_bot.print_board import print_board
from new_chess_bot.search_best_move import search_best_move

fen1 = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
fen2 = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'

fen = get_fen(get_position('https://lichess.org/uyic0uK9'))

print(fen)
print_board(fen)
print(search_best_move(fen))