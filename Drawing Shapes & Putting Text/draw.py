import cv2 as cv
import numpy as np

# img = cv.imread('../src/img.png')
# cv.imshow('Mountain', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# paint image
# blank[:] = 0, 0, 225
# cv.imshow('RED', blank)

# square
# blank[200:300, 300:400] = 0, 0, 225
# cv.imshow('RED Square', blank)

# rectangle - 1
# cv.rectangle(blank, (5, 5), (150, 200), (0, 255, 0), thickness=-1)  # thickness=cv.FILLED
# cv.imshow('Rectangle', blank)

# rectangle - 2
# cv.rectangle(blank, (5, 5), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle', blank)

# circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 225), thickness=-1)
# cv.imshow('Circle', blank)

# line
# cv.line(blank, (100, 100), (300, 500), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# text
cv.putText(blank, 'Hi Programmer', (25, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
