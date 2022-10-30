# Syntax: cv2.ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color [, thickness[, lineType[, shift]]])

# Parameters:
# image: It is the image on which ellipse is to be drawn.
# centerCoordinates: It is the center coordinates of ellipse. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# axesLength: It contains tuple of two variables containing major and minor axis of ellipse (major axis length, minor axis length).
# angle: Ellipse rotation angle in degrees.
# startAngle: Starting angle of the elliptic arc in degrees.
# endAngle: Ending angle of the elliptic arc in degrees.
# color: It is the color of border line of shape to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the shape border line in px. Thickness of -1 px will fill the shape by the specified color.
# lineType: This is an optional parameter.It gives the type of the ellipse boundary.
# shift: This is an optional parameter. It denotes the number of fractional bits in the coordinates of the center and values of axes.

# Return Value: It returns an image.

# Python program to explain cv2.ellipse() method
	
# importing cv2
import cv2
	
# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
	
# Reading an image in default mode
image = cv2.imread(path)
	
# Window name in which image is displayed
window_name = 'Image'

center_coordinates = (115, 115)

axesLength = (100, 50)

angle = 0

startAngle = 0

endAngle = 360

# Red color in BGR
color = (0, 0, 255)

# Line thickness of 1 px (-1:filling)
thickness = 2

# Using cv2.ellipse() method
# Draw a ellipse with red line borders of thickness of 5 px
image = cv2.ellipse(image, center_coordinates, axesLength,
		angle, startAngle, endAngle, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
