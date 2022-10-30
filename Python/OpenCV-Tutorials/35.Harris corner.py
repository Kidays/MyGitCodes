# Syntax: cv2.cornerHarris(src, dest, blockSize, kSize, freeParameter, borderType)
# Parameters: 
# src – Input Image (Single-channel, 8-bit or floating-point) 
# dest – Image to store the Harris detector responses. Size is same as source image 
# blockSize – Neighborhood size ( for each pixel value blockSize * blockSize neighbourhood is considered ) 
# ksize – Aperture parameter for the Sobel() operator 
# freeParameter – Harris detector free parameter 
# borderType – Pixel extrapolation method ( the extrapolation mode used returns the coordinate of the pixel corresponding to the specified extrapolated pixel )

# Python program to illustrate
# corner detection with
# Harris Corner Detection Method

# organizing imports
import cv2
import numpy as np

# path to input image specified and
# image is loaded with imread command
image = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\corner.png')

# convert the input image into
# grayscale color space
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# modify the data type
# setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

# Reverting back to the original image,
# with optimal threshold value
image[dest > 0.01 * dest.max()]=[0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', image)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
