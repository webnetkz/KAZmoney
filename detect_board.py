import cv2


shot = cv2.imread("screenshot.png")

h = 830
w = 830

left = 520
top = 173

crop_img = shot[top:top + h, left:left + w]

cv2.imshow("T", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
