import sys
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'https://lichess.org/x6Y9nRig'

def get_position(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Инициализируем словарь, в котором будем хранить позиции фигур на доске
        piece_positions = {}

        # Ищем все элементы "piece" и извлекаем их классы и стили
        piece_elements = soup.find_all('piece')
        for piece in piece_elements:
            piece_class = piece['class'][-1]
            piece_color = piece['class'][0]
            style = piece['style']

            top_percent = float(style.split(';')[0].split(':')[1].replace('%', ''))
            left_percent = float(style.split(';')[1].split(':')[1].replace('%', ''))

            # Преобразуем проценты в координаты клетки на шахматной доске
            row = int((100 - top_percent) / 12.5)
            column = int(left_percent / 12.5)
            cell_name = chr(97 + column) + str(row)  # Преобразуем в формат "a1", "b2" и т.д.

            # Определяем цвет фигуры
            if piece_color == 'white':
                color = 'white'
            else:
                color = 'black'
            
            # Записываем в словарь с указанием как цвет, так и класс фигуры
            piece_positions[cell_name] = f"{color} {piece_class}"

        # Выводим словарь с позициями фигур
        # for cell, piece_class in piece_positions.items():
        #     print(f'{cell} = {piece_class}')

        return piece_positions

    else:
        print(f'Ошибка при запросе: {response.status_code}')


print(get_position(url))