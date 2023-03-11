import os
import cv2
import numpy as np

import cv2
import numpy as np

def remove_color_from_image(img):
    # Получаем размеры изображения
    height, width, _ = img.shape


    # Получаем средний цвет на пересечении 4-х точек
    color = np.mean(img[3,3] , axis=0)

    # Преобразуем изображение в формат HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Получаем маску для фона
    lower = np.array([color[0]-10, 0.6*color[1], 0.6*color[2]])
    upper = np.array([color[0]+10, 1.4*color[1], 1.4*color[2]])
    mask = cv2.inRange(hsv, lower, upper)

    # Используем морфологические операции для устранения шумов
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Используем маску для удаления фона на изображении
    result = cv2.bitwise_and(img, img, mask=mask)

    return result



input_folder = 'images/figures/'
output_folder = 'processed/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # Загружаем изображение
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # Удаляем фоновый цвет
        processed_image = remove_color_from_image(image)

        # Сохраняем обработанное изображение
        output_filepath = os.path.join(output_folder, filename)
        cv2.imwrite(output_filepath, processed_image)
