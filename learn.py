import cv2
import numpy as np

# Создание трека
def changeGray():
    pass


cv2.namedWindow("track")
cv2.createTrackbar("Gray", "track", 0, 255, changeGray)
cv2.createTrackbar("Canny", "track", 0, 255, changeGray)



img = cv2.imread("screenshot.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


trash1 = cv2.getTrackbarPos("Gray", "track")
trash2 = cv2.getTrackbarPos("Canny", "track")


canny = cv2.Canny(gray, trash1, trash2)
cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 255), thickness=12)
cv2.circle(img, (300, 500), (100), (0, 0, 255), thickness=1)
cv2.line(img, (300, 500), (100, 0), (0, 0, 255), thickness=1)
cv2.putText(img, "TEXT", (1300, 1000), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)


cv2.imshow("t", img)
cv2.waitKey(0)