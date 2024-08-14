import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Reading the image using OpenCV
image = cv2.imread("sri.jpg")

# Convert the image to grayscale using OpenCV
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a figure and axes for displaying images
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Display the original image
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying with Matplotlib
axes[0].set_title('Original Image')
axes[0].axis('off')

# Calculate the negative image
negative_image = 255 - gray_image

# Display the negative image
axes[1].imshow(negative_image, cmap='gray')
axes[1].set_title('Negative Image')
axes[1].axis('off')

# Thresholding using PIL
img = Image.open("sri.jpg")
threshold = 50
img_threshold = img.point(lambda x: 255 if x > threshold else 0)

# Display the thresholded image
axes[2].imshow(img_threshold, cmap='gray')
axes[2].set_title('Thresholded Image')
axes[2].axis('off')

plt.show()

 

#Bit Plane Slicing
import numpy as np
import cv2

def int2bitarray(img):
    arr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            arr.append(np.binary_repr(img[i, j], width=8))
    return np.array(arr)

def bit_plane_slicing(image):
    # Convert image to bitstream array
    arr = int2bitarray(image)
    arr = arr.reshape(image.shape)
    
    # Initialize plane array
    plane = np.zeros((8, image.shape[0], image.shape[1]), dtype=int)
    
    # Fill plane array
    for k in range(8):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                plane[k, i, j] = int(arr[i, j][k])
    
    temp = np.zeros((plane.shape[1], plane.shape[2]), dtype=int)
    
    # Process bit planes
    for k in range(1, 7):  # Assuming we want to iterate through some specific planes
        for i in range(plane.shape[1]):
            for j in range(plane.shape[2]):
                if k == 1:
                    # bitplanes 7 and 6
                    temp[i, j] = (plane[k-1, i, j] << 7) | (plane[k, i, j] << 6)
                elif k == 2:
                    # bitplanes 7, 6, and 5
                    temp[i, j] = (plane[k-2, i, j] << 7) | (plane[k-1, i, j] << 6) | (plane[k, i, j] << 5)
                elif k == 3:
                    # bitplanes 7, 6, 5, and 4
                    temp[i, j] = (plane[k-3, i, j] << 7) | (plane[k-2, i, j] << 6) | (plane[k-1, i, j] << 5) | (plane[k, i, j] << 4)
                elif k == 4:
                    # bitplanes 7, 6, 5, 4, and 3
                    temp[i, j] = (plane[k-4, i, j] << 7) | (plane[k-3, i, j] << 6) | (plane[k-2, i, j] << 5) | (plane[k-1, i, j] << 4) | (plane[k, i, j] << 3)
                # Add more conditions here if needed
                
    # Save the modified image
    output_filename = 'bitplanes_output.png'
    cv2.imwrite(output_filename, temp)
    
    # Display the result
    result_image = cv2.imread(output_filename)
    cv2.imshow('Result Image', result_image)
    cv2.waitKey(0)  # Wait for any key to be pressed
    cv2.destroyAllWindows()

# Load your image
image = cv2.imread('sri.jpg', cv2.IMREAD_GRAYSCALE)
if image is not None:
    bit_plane_slicing(image)
else:
    print("Error loading image")
