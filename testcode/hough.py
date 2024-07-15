import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
kernel = np.ones((3,3), np.uint8)

edges = cv2.Canny(gray,50,200,apertureSize = 3)
#edges = cv2.dilate(edges, kernel,iterations = 1)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges,1,np.pi/180,200)

#lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

##for line in lines:
##    x1,y1,x2,y2 = line[0]
##    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

print(len(lines))
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1), (x2,y2), (0, 0, 255), 2)

#`cv2.imwrite('houghlines3.jpg',img)
cv2.imshow('Lines', img);
cv2.waitKey(0)
cv2.destroyAllWindows()
