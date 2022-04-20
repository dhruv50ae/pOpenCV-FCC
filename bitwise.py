import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), "uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("BAnd", bitwise_and)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BOr", bitwise_or)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BXor", bitwise_xor)
bitwise_notR = cv.bitwise_not(rectangle)
cv.imshow("BNotR", bitwise_notR)
bitwise_notC = cv.bitwise_not(circle)
cv.imshow("BNotC", bitwise_notC)

cv.waitKey(0)
