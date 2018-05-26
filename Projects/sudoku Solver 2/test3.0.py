from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2
i = 0
image = cv2.imread("sudoku.jpg")
#blurred = cv2.pyrMeanShiftFiltering(image,31,91)
blurred = cv2.medianBlur(image,9)
gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
#blurred = cv2.medianBlur(gray,5)
th3 = cv2.adaptiveThreshold(gray,200,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,3)
edged = cv2.Canny(th3,100,200)
_,contours,_ = cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea,reverse=True)
# cv2.drawContours(image,contours,0,(0,0,255),3)
#print(len(contours))
for c in contours:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)

    if(len(approx)==4):
        screenCnt= approx
        break
cv2.drawContours(image,screenCnt,0,(0,0,255),3)
'''
warped = four_point_transform(image,screenCnt)
t = threshold_local(warped,11,offset=10,method="gaussian")
warped = (warped>t).astype("uint8")*255
'''
#cv2.imshow('edged',imutils.resize(image,height = 650))
cv2.imshow("Edged",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
