import cv2
import matplotlib.pyplot as plt
# Read the image
original_image = cv2.imread('Slime.png', cv2.IMREAD_GRAYSCALE)

# Resize the image
desired_width = 420
desired_height = 420
resized_image = cv2.resize(original_image, (desired_width, desired_height))

# Apply Otsu thresholding
_, binary_image = cv2.threshold(resized_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Display the images using matplotlib
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Display original image
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

# Display resized image
axes[1].imshow(resized_image, cmap='gray')
axes[1].set_title('Resized Image')
axes[1].axis('off')

# Display binary image
axes[2].imshow(binary_image, cmap='gray')
axes[2].set_title('Binary Image')
axes[2].axis('off')
plt.show()
