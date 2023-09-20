import cv2
import dlib
import numpy as np

# Загрузка предобученной модели для обнаружения лиц
detector = dlib.get_frontal_face_detector()
# Загрузка предобученной модели для обнаружения ключевых точек лица (включая глаза)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Запуск видеопотока с веб-камеры (0 - основная камера)
cap = cv2.VideoCapture(0)

while True:
    # Считывание кадра с веб-камеры
    ret, frame = cap.read()
    
    # Обнаружение лиц на кадре
    faces = detector(frame)
    
    for face in faces:
        # Обнаружение ключевых точек лица, включая глаза
        landmarks = predictor(frame, face)
        
        # Получение координат внутренних и внешних краев глаз
        left_eye_inner = landmarks.part(39)
        left_eye_outer = landmarks.part(36)
        right_eye_inner = landmarks.part(42)
        right_eye_outer = landmarks.part(45)
        
        # Получение координат зрачков глаз
        left_eye_pupil = landmarks.part(37)
        right_eye_pupil = landmarks.part(44)
        
        # Вычисление координат центров краев глаз
        left_eye_inner_center = (left_eye_inner.x, left_eye_inner.y)
        left_eye_outer_center = (left_eye_outer.x, left_eye_outer.y)
        right_eye_inner_center = (right_eye_inner.x, right_eye_inner.y)
        right_eye_outer_center = (right_eye_outer.x, right_eye_outer.y)
        
        # Вычисление координат центров зрачков глаз
        left_eye_pupil_center = (left_eye_pupil.x + 7, left_eye_pupil.y + 5)
        right_eye_pupil_center = (right_eye_pupil.x - 7, right_eye_pupil.y + 5)
        
        # Рисование точек в центрах краев глаз
        cv2.circle(frame, left_eye_inner_center, 1, (0, 0, 255), -1)
        cv2.circle(frame, left_eye_outer_center, 1, (0, 0, 255), -1)
        cv2.circle(frame, right_eye_inner_center, 1, (0, 0, 255), -1)
        cv2.circle(frame, right_eye_outer_center, 1, (0, 0, 255), -1)
        
        # Рисование точек на зрачках глаз
        cv2.circle(frame, left_eye_pupil_center, 1, (0, 255, 0), -1)
        cv2.circle(frame, right_eye_pupil_center, 1, (0, 255, 0), -1)
    
    # Отображение кадра с лицами, глазами и точками
    cv2.imshow("Eye Tracking", frame)
    
    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов и закрытие окон
cap.release()
cv2.destroyAllWindows()
