import cv2

img = cv2.imread("../src/img.png", 0)

cv2.imwrite("toImg.png", img)
cv2.imshow("Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
