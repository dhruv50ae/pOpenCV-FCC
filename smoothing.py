import cv2 as cv

img = cv.imread("Photos/dog1.jpg")
cv.imshow("Dog", img)

average = cv.blur(img, (7, 7))
cv.imshow("Average", average)

gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gauss", gauss)

median = cv.medianBlur(img, 7)
cv.imshow("Median", median)

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
