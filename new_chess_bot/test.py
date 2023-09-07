from get_position import get_position
from get_fen import get_fen
from print_board import print_board
from search_best_move import search_best_move


fen = get_fen(get_position('https://lichess.org/uyic0uK9r1PT'))
print(search_best_move(fen))
#print_board(fen)