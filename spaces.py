import cv2 as cv

img = cv.imread("Photos/dog1.jpg")
cv.imshow("Dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_BGR2HSV)
cv.imshow("HSV_BGR", hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_BGR2LAB)
cv.imshow("lab_BGR", lab_bgr)

cv.waitKey(0)
