# Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)

# Parameters: 
# src: It is the source image. 
# top: It is the border width in number of pixels in top direction. 
# bottom: It is the border width in number of pixels in bottom direction. 
# left: It is the border width in number of pixels in left direction. 
# right: It is the border width in number of pixels in right direction. 
# borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc dest: It is the destination image
# value: It is an optional parameter which depicts color of border if border type is cv2.BORDER_CONSTANT.

# Return Value: It returns an image. 

# The borderType flags are described below:

# cv2.BORDER_CONSTANT: It adds a constant colored border. The value should be given as a keyword argument
# cv2.BORDER_REFLECT: The border will be mirror reflection of the border elements. Suppose, if image contains letters “abcdefg” then output will be “gfedcba|abcdefg|gfedcba“. 
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT: It does the same works as cv2.BORDER_REFLECT but with slight change. Suppose, if image contains letters “abcdefgh” then output will be “gfedcb|abcdefgh|gfedcba“. 
# cv2.BORDER_REPLICATE: It replicates the last element. Suppose, if image contains letters “abcdefgh” then output will be “aaaaa|abcdefgh|hhhhh“. 
# Python program to explain cv2.copyMakeBorder() method

# importing cv2
import cv2

# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.copyMakeBorder() method
# image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = (255,255,255))
image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

