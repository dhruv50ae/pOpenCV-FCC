import cv2 as cv

img = cv.imread("Photos/dog1.jpg")
cv.imshow("Dog", img)

cv.waitKey(0)
