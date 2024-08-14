import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread("bruno.jpg")

# OpenCV reads images in BGR format, convert it to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Creating the kernel with numpy
kernel2 = np.ones((3, 3), np.float32) / 9

# Applying the filter for smoothing
smoothed_img = cv2.filter2D(src=image_rgb, ddepth=-1, kernel=kernel2)

# Defining kernel for sharpening
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]]) / 9

sharpened = cv2.filter2D(image_rgb, -1, kernel)

# Display the images
plt.subplot(131), plt.imshow(image_rgb), plt.title('Original')
plt.subplot(132), plt.imshow(smoothed_img), plt.title('Smoothing')
plt.subplot(133), plt.imshow(sharpened), plt.title('Sharpening')

plt.show()

 
