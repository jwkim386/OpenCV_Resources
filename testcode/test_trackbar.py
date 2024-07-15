import cv2

def onChange(pos):
    pass

src = cv2.imread("sudoku.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Trackbar Windows")

cv2.createTrackbar("threshold", "Trackbar Windows", 0, 255, onChange)
cv2.createTrackbar("maxValue", "Trackbar Windows", 0, 255, lambda x : x)

cv2.setTrackbarPos("threshold", "Trackbar Windows", 127)
cv2.setTrackbarPos("maxValue", "Trackbar Windows", 255)

while cv2.waitKey(1) != ord('q'):

    thresh = cv2.getTrackbarPos("threshold", "Trackbar Windows")
    maxval = cv2.getTrackbarPos("maxValue", "Trackbar Windows")

    _, binary = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)

    cv2.imshow("Trackbar Windows", binary)

cv2.destroyAllWindows()
