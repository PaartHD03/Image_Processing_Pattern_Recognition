import cv2
import numpy as np

# Load the image
image = cv2.imread("uwp3710233.jpeg")

# Convert image to floating point
pixels = np.float32(image.reshape((-1, 3)))

# Define criteria and apply k-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 2
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back to uint8
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]

# Reshape the segmented image to match the original image shape
segmented_image = segmented_image.reshape(image.shape)

# Display the original and segmented images
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
