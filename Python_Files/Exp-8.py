import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
def load_image(file_path, threshold=128, size=None):
    # Open the image directly from the disk
    img = Image.open(file_path).convert('L')  # Convert to grayscale
    if size:
        img = img.resize(size)
    img_np = np.array(img)
    img_binary = np.where(img_np > threshold, 1, 0)  # Convert to binary
    return img_binary

def display_image(image, title="Image"):
    plt.figure(figsize=(5, 5))
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.axis('off')
    plt.show()
def erosion(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    output = np.zeros_like(image)
    pad_height, pad_width = kernel_height // 2, kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    for i in range(image_height):
        for j in range(image_width):
            if np.all(kernel == padded_image[i:i+kernel_height, j:j+kernel_width] * kernel):
                output[i, j] = 1
    return output

def dilation(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    output = np.zeros_like(image)
    pad_height, pad_width = kernel_height // 2, kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    for i in range(image_height):
        for j in range(image_width):
            if np.any(kernel == padded_image[i:i+kernel_height, j:j+kernel_width] * kernel):
                output[i, j] = 1
    return output
# Path to your local image file
image_path = 'NAMEPLAT.png'  # Adjust this to the path of your image

# Load and display the original binary image
binary_image = load_image(image_path, threshold=128, size=(256, 256))
display_image(binary_image, "Original Binary Image")

# Define a simple kernel for morphological operations
kernel = np.ones((3, 3), dtype=np.uint8)

# Apply erosion
eroded_image = erosion(binary_image, kernel)
display_image(eroded_image, "Eroded Image")

# Apply dilation
dilated_image = dilation(binary_image, kernel)
display_image(dilated_image, "Dilated Image")
