import cv2 as cv

capture = cv.VideoCapture('../src/Skate.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('p'):
        break

capture.relase()
cv.destroyAllWindows()
