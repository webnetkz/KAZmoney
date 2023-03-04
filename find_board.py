# import cv2

# def find_chessboard_corner(image_path):
#     # загрузка изображения
#     img = cv2.imread(image_path)

#     # применение фильтра Гаусса
#     blurred = cv2.GaussianBlur(img, (5, 5), 0)

#     # выделение границ объектов на изображении с помощью алгоритма Canny
#     edges = cv2.Canny(blurred, 100, 200)

#     # поиск контуров на изображении
#     contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # нахождение контура, соответствующего шахматной доске
#     chessboard_contour = None
#     for contour in contours:
#         # аппроксимация контура
#         approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)

#         # проверка, является ли контур прямоугольником
#         if len(approx) == 4 and cv2.isContourConvex(approx):
#             x, y, w, h = cv2.boundingRect(contour)
#             aspect_ratio = float(w)/h
#             if aspect_ratio >= 0.8 and aspect_ratio <= 1.2:
#                 chessboard_contour = approx
#                 break

#     if chessboard_contour is not None:
#         # нахождение координат левого верхнего угла контура
#         leftmost = tuple(chessboard_contour[chessboard_contour[:,:,0].argmin()][0])
#         topmost = tuple(chessboard_contour[chessboard_contour[:,:,1].argmin()][0])


#         cv2.imshow('image', img)
#         cv2.waitKey(0)
#         return topmost
#     else:
#         return None

import tkinter as tk

root = tk.Tk()
width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()
root.destroy()

print("Ширина монитора: {} пикселей".format(width_px))
print("Высота монитора: {} пикселей".format(height_px))
