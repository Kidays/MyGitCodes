# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeksforgeeks.png', 0)

# find frequency of pixels in range 0-255
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()

# _________________________________________

img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeksforgeeks.png', 0)

# alternative way to find histogram of an image
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
