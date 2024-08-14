import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread('elu.jpeg', 0)

# Calculate histogram of the original image
hist, bins = np.histogram(img.flatten(), 256, [0,256])

# Calculate cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Perform histogram equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255 / (cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# Apply the equalization on the image
img_equalized = cdf[img]

# Calculate histogram of the equalized image
hist_equalized, bins_equalized = np.histogram(img_equalized.flatten(), 256, [0,256])

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(2, 2, 2), plt.plot(hist, color='r'), plt.title('Histogram of Original Image')

plt.subplot(2, 2, 3), plt.imshow(img_equalized, cmap='gray'), plt.title('Equalized Image')
plt.subplot(2, 2, 4), plt.plot(hist_equalized, color='r'), plt.title('Histogram of Equalized Image')

plt.tight_layout()
plt.show()
