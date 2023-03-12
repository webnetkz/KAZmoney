import cv2

def match_images(image1_path, image2_path, priznaks):
    # Загружаем изображения
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Создаем объект ORB
    orb = cv2.ORB_create()

    # Находим ключевые точки и дескрипторы для каждого изображения
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Создаем объект Matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Находим соответствия между ключевыми точками двух изображений
    matches = bf.match(des1, des2)

    # Сортируем соответствия по расстоянию между дескрипторами
    matches = sorted(matches, key=lambda x: x.distance)

    # Проверяем, есть ли хотя бы 6 соответствий
    if len(matches) >= priznaks:
        return True
    else:
        return False
    
# Функция для поиска совпадающих контуров на двух изображениях
def find_matching_contours(img1_path, img2_path):
    # Загрузка изображений
    img1 = cv2.imread(img1_path)
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img2 = cv2.imread(img2_path)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Проверка соответствия цветов
    img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    img1_mean = cv2.mean(img1_hsv)
    img2_mean = cv2.mean(img2_hsv)
    for i in range(3):
        if abs(img1_mean[i] - img2_mean[i]) / 255 > 0.1:
            return False

    # Поиск контуров на изображениях
    contours1, _ = cv2.findContours(img1_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(img2_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Поиск совпадающих контуров
    matching_contours = []
    for c1 in contours1:
        for c2 in contours2:
            match = cv2.matchShapes(c1, c2, cv2.CONTOURS_MATCH_I1, 0)
            if match < 0.1:
                matching_contours.append(c1)
                break

    if len(matching_contours) > 0:
        return True
    else:
        return False






# Загружаем изображения
# img1 = './images/figures/b_rook_b.png'
# img2 = './images/figures/w_rook_w.png'

# print(find_matching_contours(img1, img2))