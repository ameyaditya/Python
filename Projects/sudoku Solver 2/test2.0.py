from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

image = cv2.imread("sudoku.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray,5)
th3 = cv2.adaptiveThreshold(blurred,200,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,17,5)
edged = cv2.Canny(th3,100,200)

cv2.imshow('edged',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
