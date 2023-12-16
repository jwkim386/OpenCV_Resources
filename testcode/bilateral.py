import cv2

# Read the sample image
img = cv2.imread("fabric-textures.jpg")

#print(img.shape)

# Display the original image
cv2.imshow("Original Image", img)

# Apply bilateral filter to reduce noise while preserving edges
filtered_img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

# Display the filtered image
cv2.imshow("Filtered Image", filtered_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
