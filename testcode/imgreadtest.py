import cv2
import sys

img = cv2.imread("starry_night.jpg")

if img is None:
	sys.exit("Could not read the image.")

cv2.imshow("Display window", img)
k = cv2.waitKey(0)

if k == ord("s"):
	cv2.imwrite("starry_night.png", img)
cv2.destroyAllWindows()