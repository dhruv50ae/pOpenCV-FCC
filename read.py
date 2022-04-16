import cv2 as cv

# img = cv.imread('Photos/dog1.jpg')

# cv.imshow("Dog", img)

capture = cv.VideoCapture('Videos/doge.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows

# cv.waitKey(0)
