import cv2 as cv

img = cv.imread("Photos/dog1.jpg")
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/doge.mp4')

while True:
    isTrue, frame = capture.read()

    frameResized = rescaleFrame(frame, scale=0.5)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frameResized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows
