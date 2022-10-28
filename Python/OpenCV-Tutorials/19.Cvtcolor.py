# Syntax: cv2.cvtColor(src, code[, dst[, dstCn]])

# Parameters:
# src: It is the image whose color space is to be changed.
# code: It is the color space conversion code.
# dst: It is the output image of the same size and depth as src image. It is an optional parameter.
# dstCn: It is the number of channels in the destination image. If the parameter is 0 then the number of the channels is derived automatically from src and code. It is an optional parameter.

# Return Value: It returns an image.

# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )

# Displaying the image
cv2.imshow(window_name, image)

# De-allocate any associated memory usage		
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()	


#________________________________________________

# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )

# Displaying the image
cv2.imshow(window_name, image)
# De-allocate any associated memory usage		
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()	