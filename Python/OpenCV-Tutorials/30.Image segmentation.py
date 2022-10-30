# Python program to transform an image using
# threshold.
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255,
							cv2.THRESH_BINARY_INV +
							cv2.THRESH_OTSU)

# Noise removal using Morphological
# closing operation
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
							kernel, iterations = 1)

# Background area using Dilation
bg = cv2.dilate(closing, kernel, iterations = 11)

# Finding foreground area
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.01
						* dist_transform.max(), 255, 0)
(h,w)=fg.shape[:2]
img1=cv2.resize(fg,(int(w/4),int(h/4)))
cv2.imshow('image', img1)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()