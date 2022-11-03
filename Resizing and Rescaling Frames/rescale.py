import cv2 as cv


# Rescale function
def rescaleFrame(frame, scale=0.75):
    # image, video, live video
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dimensions = (w, h)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRescaleFrame(w, h):
    # live video
    capture.set(3, w)
    capture.set(4, h)


# Image
img = cv.imread('../src/img.png')
img_frame_resized = rescaleFrame(img)
cv.imshow('Mountain Resized', img_frame_resized)
cv.imshow('Mountain', img)

# Video
capture = cv.VideoCapture('../src/Skate.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.3)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('p'):
        break

capture.relase()
cv.destroyAllWindows()

cv.waitKey(0)
