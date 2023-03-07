import numpy as np
import cv2
import pyautogui
from PIL import ImageGrab


def create_clear_matrix():
    # Получаем размеры экрана
    screen_width, screen_height = pyautogui.size()

    # Создаем пустое черное изображение
    black_image = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
    return black_image

def process_image():
    # Захват скриншота экрана
    img = ImageGrab.grab()

    # Преобразование изображения в массив numpy и перевод в серый цвет
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # Применение фильтра Гаусса для уменьшения шума на изображении
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)

    # Обнаружение горизонтальных и вертикальных линий на изображении
    edges = cv2.Canny(blurred, 50, 50, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=100, maxLineGap=5)

    matrix_img = create_clear_matrix()

    # Рисование линий на изображении
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_np, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.line(matrix_img, (x1, y1), (x2, y2), (0, 0, 255), 1)


    # Вывод изображения с маркерами
    cv2.imshow("Image", img_np)
    cv2.waitKey(0)
    # Вывод изображения с маркерами
    cv2.imshow("Image", matrix_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

process_image()
