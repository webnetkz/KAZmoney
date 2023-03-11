import cv2

def match_images(image1_path, image2_path):
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
    if len(matches) >= 12:
        return True
    else:
        return False


# Загружаем изображения
img1 = './images/figures/w_horse_b.png'
img2 = './images/figures/w_horse_w.png'

print(match_images(img1, img2))