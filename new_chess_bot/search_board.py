import cv2
import numpy as np
import pyautogui

def find_chessboard_on_screen():
    # Задайте размер области, которую вы хотите сканировать (в пикселях)
    screen_width, screen_height = pyautogui.size()
    region = (0, 0, screen_width, screen_height)

    # Загрузка каскада Хаара для шахматной доски
    chessboard_cascade = cv2.CascadeClassifier('chessboard.xml')

    while True:
        # Захватите изображение с экрана в указанной области
        screenshot = pyautogui.screenshot(region=region)

        # Преобразовать скриншот в массив numpy
        screen_img = np.array(screenshot)

        # Преобразовать изображение в оттенки серого
        gray_img = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)

        # Найти шахматную доску на изображении
        chessboards = chessboard_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

        # Если найдена хотя бы одна доска, вывести координаты
        if len(chessboards) > 0:
            for (x, y, w, h) in chessboards:
                print(f"Шахматная доска найдена на координатах: x={x}, y={y}, ширина={w}, высота={h}")
                # Вы можете выполнить другие действия с найденной доской здесь

        # Если не найдено ни одной доски, вывести сообщение
        if len(chessboards) == 0:
            print("Шахматная доска не найдена на экране.")

        # Ожидание некоторого времени перед следующей проверкой
        cv2.waitKey(1000)  # Подождать 1 секунду

if __name__ == "__main__":
    find_chessboard_on_screen()
