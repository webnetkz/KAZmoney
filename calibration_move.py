import numpy as np
import pyautogui as pg
import time
import subprocess

# Получение стартовой позиции и ширины шахматной доски
from find_board import get_start_position
position_board = get_start_position()

# Константы для работы бота
BOARD_SIZE = position_board[2]-4
DARK_SQUARE_THRESHOLD = 160
CELL_SIZE = int(BOARD_SIZE / 8)
BOARD_TOP_COORD = position_board[1]+4
BOARD_LEFT_COORD = position_board[0]+3

def go_move():

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
  ]

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


  best_move = "d2d3"
  # Получает позицию квадратов для хода
  from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
  to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

  # Совершает ход
  pg.moveTo(from_sq)
  pg.click()
  pg.moveTo(to_sq)
  pg.click()
  time.sleep(3)

  best_move = "d1d2"
  # Получает позицию квадратов для хода
  from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
  to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

  # Совершает ход
  pg.moveTo(from_sq)
  pg.click()
  pg.moveTo(to_sq)
  pg.click()
  time.sleep(3)

  best_move = "e2e3"
  # Получает позицию квадратов для хода
  from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
  to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

  # Совершает ход
  pg.moveTo(from_sq)
  pg.click()
  pg.moveTo(to_sq)
  pg.click()
  time.sleep(3)

  best_move = "e1e2"
  # Получает позицию квадратов для хода
  from_sq = square_to_coords[get_square.index(best_move[0] + best_move[1])]
  to_sq = square_to_coords[get_square.index(best_move[2] + best_move[3])]

  # Совершает ход
  pg.moveTo(from_sq)
  pg.click()
  pg.moveTo(to_sq)
  pg.click()
  time.sleep(3)
  subprocess.run(['python3', 'find_king_queen.py'])


go_move()