# -*- coding: utf-8 -*-
# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import chess
import chess.engine
import pyautogui as pg
import time
import tkinter as tk
from move_best import move


options = webdriver.ChromeOptions() # Создание объекта настроек
options.add_argument('headless') # Активация скрытого режима
EXE_PATH = r"C:\chromedriver.exe" # Путь до драйвера
driver = webdriver.Chrome(executable_path=EXE_PATH) #, chrome_options=options)
driver.get('https://lichess.org/')


def get_chess_square(x, y):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [8, 7, 6, 5, 4, 3, 2, 1]
    
    file_index = x // 99
    rank_index = y // 99
    
    file = letters[file_index]
    rank = numbers[rank_index]
    
    return file + str(rank)


def get_pieces_from_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    pieces = soup.select('piece.white, piece.black')
    result = []
    for piece in pieces:
        piece_color = piece.get('class')[0]
        piece_class = piece.get('class')[1]
        style = piece.get('style')
        match = re.search(r'translate\((\d+)px,\s*(\d+)px\)', style)
        x, y = match.groups()
        position = get_chess_square(int(x), int(y))
        result.append(f"{piece_color} {piece_class} - {position}")
    return result


def board_to_fen(board):
    fen = ""
    for row in board:
        empty_squares = 0
        for cell in row:
            if cell == " ":
                empty_squares += 1
            else:
                if empty_squares > 0:
                    fen += str(empty_squares)
                    empty_squares = 0
                fen += cell
        if empty_squares > 0:
            fen += str(empty_squares)
        fen += "/"
    return fen[:-1]  # Убираем последний символ ("/")


def place_piece(board, piece, position):
    col = ord(position[0]) - ord("a")
    row = 8 - int(position[1])
    board[row][col] = piece


# Находит лучший ход
def search(fen):
    board = chess.Board(fen=fen)
    engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
    best_move = str(engine.play(board, chess.engine.Limit(time=1)).move)
    engine.quit()
    return best_move


def find_pieces(html, pos):
    soup = BeautifulSoup(html, 'html.parser')
    piece = soup.find('piece', {'style': f'transform: translate({pos});'})
    selector = 'piece[{}]'.format(','.join([f"{k}='{v}'" for k, v in piece.attrs.items() if k != 'class']))
    return selector


def getAllPositions(color):
    pieces = get_pieces_from_html(driver.page_source)

    board = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]
    ]

    for pos in pieces:
        piece, square = pos.split(" - ")

        if piece == "white pawn":
          place_piece(board, "P", square)
        elif piece == "black pawn":
          place_piece(board, "p", square)
        elif piece == "white rook":
          place_piece(board, "R", square)
        elif piece == "white bishop":
          place_piece(board, "B", square)
        elif piece == "white knight":
          place_piece(board, "N", square)
        elif piece == "white queen":
          place_piece(board, "Q", square)
        elif piece == "white king":
          place_piece(board, "K", square)
        elif piece == "black rook":
          place_piece(board, "r", square)
        elif piece == "black bishop":
          place_piece(board, "b", square)
        elif piece == "black knight":
          place_piece(board, "n", square)
        elif piece == "black queen":
          place_piece(board, "q", square)
        elif piece == "black king":
          place_piece(board, "k", square)


    fen = board_to_fen(board)
    fen += " "+color+" KQkq - 0 1"
    best_move = search(fen)
    print(best_move)
    move(best_move)



root = tk.Tk()

var = tk.StringVar(value="w")  # по умолчанию выбрано значение "w"

white_button = tk.Radiobutton(root, text="Белые", variable=var, value="w")
black_button = tk.Radiobutton(root, text="Черные", variable=var, value="b")
button = tk.Button(root, text="Ход", command=lambda: getAllPositions(var.get()))  # используем лямбда-функцию для передачи аргумента

white_button.pack()
black_button.pack()
button.pack()

root.mainloop()




    


