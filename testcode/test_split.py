import cv2
import matplotlib.pyplot as plt

src = cv2.imread("messi5.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
inverse = cv2.merge((r, g, b))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)

plt.imshow(inverse)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
