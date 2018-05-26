from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

img = cv2.imread("rectangle.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,50,200,255)

cv2.imshow("edges",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()