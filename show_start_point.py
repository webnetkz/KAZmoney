import cv2
import numpy as np

def find_chessboard_corner(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Уменьшаем шум на изображении, используя фильтр Гаусса
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Находим углы шахматной доски
    ret, corners = cv2.findChessboardCorners(gray, (8, 8), None)

    if ret:
        # Отображаем изображение с крестиком на найденном углу
        cv2.drawMarker(img, tuple(corners[0][0]), color=(0, 0, 255), markerType=cv2.MARKER_CROSS, thickness=2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return corners[0][0]

    return None


image_path = "screenshot.png"
x, y = find_chessboard_corner(image_path)
if x is not None and y is not None:
    print(f"Левый верхний угол доски находится в точке ({x}, {y})")
else:
    print("Доска не найдена на изображении")