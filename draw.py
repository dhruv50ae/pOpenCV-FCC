import cv2 as cv
from cv2 import putText
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow("Green", blank)

# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
# cv.imshow("rectangle", blank)

# cv.circle(blank, (blank.shape[1]//2,
#           blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow("Circle", blank)

# cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=1)
# cv.imshow("Line", blank)

cv, putText(blank, "Hello World", (255, 255),
            cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)
cv.imshow("Text", blank)


cv.waitKey(0)
