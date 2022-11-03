import cv2 as cv

img = cv.imread("../src/img.png")
cv.imshow("img.png", img)

# grey
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blur
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# dilated
# dilated = cv.dilate(img, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)

# resized
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# cropped
cropped = img[100:300, 300:700]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
