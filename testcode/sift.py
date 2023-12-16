import cv2

img = cv2.imread('home.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# SIFT 추출기 생성
sift = cv2.SIFT_create()
kp = sift.detect(gray,None)

# img=cv2.drawKeypoints(gray,kp,img)
# cv2.imwrite('sift_keypoints.jpg',img)

img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT', img)
cv2.waitKey()
cv2.destroyAllWindows()
