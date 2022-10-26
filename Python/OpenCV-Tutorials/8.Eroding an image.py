# Syntax: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
# Parameters:
# src: It is the image which is to be eroded .
# kernel: A structuring element used for erosion. If element = Mat(), a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement.
# dst: It is the output image of the same size and type as src.
# anchor: It is a variable of type integer representing anchor point and it’s default value Point is (-1, -1) which means that the anchor is at the kernel center.
# borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc.
# iterations: It is number of times erosion is applied.
# borderValue: It is border value in case of a constant border.
# Return Value: It returns an image.
# Python program to explain cv2.erode() method

# importing cv2
import cv2

# importing numpy
import numpy as np

# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel = np.ones((5, 5), np.uint8)

# Using cv2.erode() method
image = cv2.erode(image, kernel)

# Displaying the image
cv2.imshow(window_name, image)
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()