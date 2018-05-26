from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2

i = 0
image = cv2.imread("sudoku.jpg")
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)
#blurred = cv2.pyrMeanShiftFiltering(image,31,91)
blurred = cv2.medianBlur(image,9)
gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
#blurred = cv2.medianBlur(gray,5)
th3 = cv2.adaptiveThreshold(gray,200,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,3)
edged = cv2.Canny(th3,100,200)
_,contours,_ = cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea,reverse=True)
cv2.drawContours(image,contours,0,(0,0,255),3)
x,y,w,h = cv2.boundingRect(contours[0])
roi = image[y:y+h,x:x+w]

warped = four_point_transform(orig, contours[0])
#cv2.imwrite("ROI1"+".jpg",roi)
cv2.imshow("image",orig)
cv2.waitKey(0)
cv2.destroyAllWindows()
