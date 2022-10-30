# Syntax : cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])

# Syntax : cv2.goodFeaturesToTrack(gray_img, maxc, Q, minD)

# Parameters :
# gray_img – Grayscale image with integral values
# maxc – Maximum number of corners we want(give negative value to get all the corners)
# Q – Quality level parameter(preferred value=0.01)
# maxD – Maximum distance(preferred value=10)

# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt


# read the image
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\corner.png')

# convert image to gray scale image,the image should be a grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 27, 0.1, 10)
corners = np.int0(corners)

# we iterate through each corner,
# making a circle at each point that we think is a corner.
# numpy.ravel(a, order='C') :Return a contiguous flattened array
# order{‘C’,’F’, ‘A’, ‘K’}, optional
for i in corners:
	x, y = i.ravel()
	cv2.circle(img, (x, y), 5, 255,-1)

plt.imshow(img), plt.show()
