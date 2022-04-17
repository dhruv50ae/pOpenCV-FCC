import cv2 as cv

img = cv.imread("Photos/dog1.jpg")

cv.imshow("Dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

dilate = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("DIalated", dilate)

erode = cv.erode(dilate, (3, 3), iterations=1)
cv.imshow("Erode", erode)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resize", resized)

cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
