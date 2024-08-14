#Display Image in python
from PIL import Image
img = Image.open("img\c.jpg")
img.show()

#  Display Format of an Image
print('Format of Image is - ',img.format)

OUTPUT :
Format of Image is -  JPEG

#Display format description
print('Description of image is - ',img.format_description)

OUTPUT :
Description of image is -  JPEG (ISO 10918)

# Display size of an image
print('Description of image is - ',img.size)

OUTPUT :
Description of image is -  (162, 148)

# Display mode of an image
print('Description of image is - ',img.mode)

OUTPUT :
Description of image is -  RGB

# pixel format used by the images. Typical values are "1" (Black N White), "L" (Greyscale), "RGB", or "CMYK."
#Convert image to grayscale OR #convert image to RGB
img = img.convert("RGB")

#save greyscale Image
img.save('greyscale_img.jpg')

#display greyscale imgage
img.show()

#display mode of greyscale image
print('Mode of grayscale is - ',img.mode)

OUTPUT :
Mode of grayscale is -  RGB

# another mode of an image another function
print('Mode of grayscale is - ',img.getbands)

OUTPUT :
Mode of grayscale is -  <bound method Image.getbands of <PIL.Image.Image image mode=RGB size=162x148 at 0x1B2B212D210>>

img_new = Image.open("img\c.jpg")
img.show()

# save as different format
img_new=img_new.save("new_image.jpg")

# display pixel data of an image
pix_val=list(img.getdata())
print('pixel value of an image :\n')
print(pix_val)



OUTPUT:
pixel value of an image :

[(252, 255, 250), (252, 255, 250), (252, 255, 250), (252, 255, 250), (252, 255, 250), (252, 255, 250), (252, 255, 250), (252, 255, 250), (254, 255, 250), (254, 255, 250), (254, 255, 250), (254, 255, 250),………


if img.mode == 'RGB':
    print('RGB component pixels values')
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            print(f'Pixel at ({x}, {y}): R={r}, G={g}, B={b}')

OUTPUT:
RGB component pixels values
Pixel at (0, 0): R=252, G=255, B=250
Pixel at (0, 1): R=254, G=255, B=250
Pixel at (0, 2): R=255, G=254, B=251
Pixel at (0, 3): R=255, G=251, B=252
Pixel at (0, 4): R=255, G=250, B=252
Pixel at (0, 5): R=255, G=249, B=253
Pixel at (0, 6): R=255, G=249, B=255
Pixel at (0, 7): R=255, G=251, B=255
Pixel at (0, 8): R=254, G=255, B=255
Pixel at (0, 9): R=246, G=254, B=255
Pixel at (0, 10): R=245, G=255, B=255
.
.
.

# Split image into RGB bands
red, green, blue = img.split()

# Merge the bands in a different sequence
img_new = Image.merge("RGB", (green, red, blue))

# Save the newly merged image
img_new.save('new_image.jpg')

# Print the mode of the newly merged image
print("\nMode of newly merged image:", img_new.mode)

# Show the newly merged image
img_new.show()
