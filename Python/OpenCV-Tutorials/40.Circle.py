# Syntax:
# cv2.circle(image, center_coordinates, radius, color, thickness)

# Parameters:
# image: It is the image on which the circle is to be drawn.
# center_coordinates: It is the center coordinates of the circle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# radius: It is the radius of the circle.
# color: It is the color of the borderline of a circle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the circle border line in px. Thickness of -1 px will fill the circle shape by the specified color.

# Return Value: It returns an image.

# Python program to explain cv2.circle() method

# importing cv2
import cv2

# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Center coordinates
center_coordinates = (120, 50)

# Radius of circle
radius = 20

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
