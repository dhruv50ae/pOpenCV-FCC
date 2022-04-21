import cv2 as cv

img = cv.imread("Photos/paris.jpg")
cv.imshow("Paris", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

threshold, threshInv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh", threshInv)

# adaptiveThresh = cv.adaptiveThreshold(
#     gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imread("AdaptiveThresh", adaptiveThresh)

# adaptiveThreshInv = cv.adaptiveThreshold(
#     gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
# cv.imread("AdaptiveThresh", adaptiveThreshInv)

cv.waitKey(0)
