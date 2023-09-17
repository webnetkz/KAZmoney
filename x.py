import cv2
import mediapipe as mp
import pyautogui

# Инициализация библиотеки Mediapipe для отслеживания взгляда
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Запуск видеопотока с веб-камеры (0 - основная камера)
cap = cv2.VideoCapture(0)

# Инициализация объекта PyAutoGUI для управления курсором
pyautogui.FAILSAFE = False

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Переворачиваем кадр по горизонтали (зависит от вашей камеры)
        frame = cv2.flip(frame, 1)

        # Обнаружение ключевых точек
        results = holistic.process(frame)

        if results.pose_landmarks:
            # Получение координат левого и правого глаз
            left_eye_x = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE].x * frame.shape[1])
            left_eye_y = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE].y * frame.shape[0])
            right_eye_x = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE].x * frame.shape[1])
            right_eye_y = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE].y * frame.shape[0])

            # Получение средней координаты глаз
            eye_x = (left_eye_x + right_eye_x) // 2
            eye_y = (left_eye_y + right_eye_y) // 2

            print(eye_x, eye_y)

            # Перемещение курсора мыши в координаты взгляда
            pyautogui.moveTo(eye_x, eye_y)

        # Отображение кадра
        cv2.imshow("Eye Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
