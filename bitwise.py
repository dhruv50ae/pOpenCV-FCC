import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), "uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("BAnd")
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BOr")
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BXor")
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("BNotR")
bitwise_not = cv.bitwise_not(circle)
cv.imshow("BNotC")
