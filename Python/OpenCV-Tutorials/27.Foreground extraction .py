# Syntax: cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, iterationCount[, mode])
# Parameters:


# image: Input 8-bit 3-channel image.
# mask: Input/output 8-bit single-channel mask. The mask is initialized by the function when mode is set to GC_INIT_WITH_RECT. Its elements may have one of following values:
# GC_BGD defines an obvious background pixels.
# GC_FGD defines an obvious foreground (object) pixel.
# GC_PR_BGD defines a possible background pixel.
# GC_PR_FGD defines a possible foreground pixel.
# rectangle: It is the region of interest containing a segmented object. The pixels outside of the ROI are marked as obvious background. The parameter is only used when mode==GC_INIT_WITH_RECT.
# backgroundModel: Temporary array for the background model.
# foregroundModel: Temporary array for the foreground model.
# iterationCount: Number of iterations the algorithm should make before returning the result. Note that the result can be refined with further calls with mode==GC_INIT_WITH_MASK or mode==GC_EVAL.
# mode: It defines the Operation mode. It can be one of the following:
# GC_INIT_WITH_RECT: The function initializes the state and the mask using the provided rectangle. After that it runs iterCount iterations of the algorithm.
# GC_INIT_WITH_MASK: The function initializes the state using the provided mask. Note that GC_INIT_WITH_RECT and GC_INIT_WITH_MASK can be combined. Then, all the pixels outside of the ROI are automatically initialized with GC_BGD.
# GC_EVAL: The value means that the algorithm should just resume.

# Python program to illustrate
# foreground extraction using
# GrabCut algorithm

# organize imports
import numpy as np
import cv2
from matplotlib import pyplot as plt

# path to input image specified and
# image is loaded with imread command
image = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\Girl.jpeg')

# create a simple mask image similar
# to the loaded image, with the
# shape and return type
mask = np.zeros(image.shape[:2], np.uint8)

# specify the background and foreground model
# using numpy the array is constructed of 1 row
# and 65 columns, and all array elements are 0
# Data type for the array is np.float64 (default)
backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

# define the Region of Interest (ROI)
# as the coordinates of the rectangle
# where the values are entered as
# (startingPoint_x, startingPoint_y, width, height)
# these coordinates are according to the input image
# it may vary for different images
rectangle = (110, 65, 410, 490)

# apply the grabcut algorithm with appropriate
# values as parameters, number of iterations = 3
# cv2.GC_INIT_WITH_RECT is used because
# of the rectangle mode is used
cv2.grabCut(image, mask, rectangle,
            backgroundModel, foregroundModel,
            11, cv2.GC_INIT_WITH_RECT)

# In the new mask image, pixels will
# be marked with four flags
# four flags denote the background / foreground
# mask is changed, all the 0 and 2 pixels
# are converted to the background
# mask is changed, all the 1 and 3 pixels
# are now the part of the foreground
# the return type is also mentioned,
# this gives us the final mask
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# The final mask is multiplied with
# the input image to give the segmented image.
image = image * mask2[:, :, np.newaxis]

# output segmented image with colorbar
plt.imshow(image)
plt.colorbar()
plt.show()
