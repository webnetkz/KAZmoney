import cv2
import numpy as np
import tensorflow as tf

# Загружаем предобученную сверточную нейронную сеть
model = tf.keras.models.load_model("chess_piece_classifier.h5")

# Список имен классов
class_names = ["пешка", "ладья", "конь", "слон", "ферзь", "король"]

def find_all_chess_pieces(image_path):
    # Загружаем изображение
    img = cv2.imread(image_path)

    # Преобразуем изображение в черно-белое
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Применяем алгоритм выделения границ Canny
    edges = cv2.Canny(gray, 100, 200)

    # Находим контуры на изображении
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Создаем список для хранения результатов
    pieces = []

    # Обходим все контуры
    for contour in contours:
        # Вычисляем прямоугольник, описывающий контур
        x, y, w, h = cv2.boundingRect(contour)

        # Обрезаем изображение по границам прямоугольника
        piece_img = img[y:y+h, x:x+w]

        # Меняем размер изображения на 64x64
        piece_img = cv2.resize(piece_img, (64, 64))

        # Преобразуем изображение в массив numpy
        piece_np = np.array(piece_img)

        # Добавляем новый размерности для соответствия входным данным нейронной сети
        piece_np = np.expand_dims(piece_np, axis=0)

        # Нормализуем значения пикселей
        piece_np = piece_np / 255.0

        # Предсказываем класс фигуры
        prediction = model.predict(piece_np)

        # Находим имя класса
        class_index = np.argmax(prediction)
        class_name = class_names[class_index]

        # Добавляем результат в список
        pieces.append((class_name, x, y, w, h))

    return pieces
