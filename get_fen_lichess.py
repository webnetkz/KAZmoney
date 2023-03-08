import lichess.api
from lichess.format import PYCHESS

game = lichess.api.game('5liMGxsM', format=PYCHESS)
print(game.end().board())
