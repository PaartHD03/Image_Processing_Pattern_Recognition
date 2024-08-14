import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image1 = cv2.imread("eye.jpeg")

# Converting because OpenCV uses BGR as default 
RGB_img = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# Converting to grayscale
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)

# Remove noise
img = cv2.GaussianBlur(gray, (3, 3), 0)

# Convolute with Sobel kernels
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5) # x
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5) # y
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5) # xy

# Plotting images
fig, ax = plt.subplots(2, 2, figsize=(17, 10))

ax[0][0].imshow(RGB_img, cmap='gray')
ax[0][0].set_title('Original Image', fontsize=18)
ax[0][0].axis('off')

ax[0][1].imshow(sobelxy, cmap='gray')
ax[0][1].set_title('Edge Detection', fontsize=18)
ax[0][1].axis('off')
ax[1][0].imshow(sobelx, cmap='gray')
ax[1][0].set_title('Sobel Operator X-Direction', fontsize=18)
ax[1][0].axis('off')

ax[1][1].imshow(sobely, cmap='gray')
ax[1][1].set_title('Sobel Operator Y-Direction', fontsize=18)
ax[1][1].axis('off')

plt.show()
