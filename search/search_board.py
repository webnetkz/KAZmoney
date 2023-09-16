import numpy as np
import cv2
import pyautogui as pg


def get_start_position():
    screen = './shot_board.png'
    pg.screenshot(screen)
    img = cv2.imread(screen)


    # Преобразование изображения в массив numpy и перевод в серый цвет
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # Применение фильтра Гаусса для уменьшения шума на изображении
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)

    # Обнаружение горизонтальных и вертикальных линий на изображении
    edges = cv2.Canny(blurred, 254, 255, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=100, maxLineGap=5)

    matrix_img = create_clear_matrix()

    # Рисование линий на изображении
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_np, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.line(matrix_img, (x1, y1), (x2, y2), (0, 0, 255), 3)


    cv2.imwrite("./images/no_bg_board.png", matrix_img)
    result_position_chess_board = find_chessboard_contour(matrix_img)

    return result_position_chess_board

# Возвращает x, y, w, h всей доски
def find_chessboard_contour(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4 and cv2.isContourConvex(approx):
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h

            if 0.9 <= aspect_ratio <= 1.1:
                return x, y, w, h

    return None

def create_clear_matrix():
    # Получаем размеры экрана
    screen_width, screen_height = pg.size()

    # Создаем пустое черное изображение
    black_image = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
    return black_image


while True:
    print(get_start_position())