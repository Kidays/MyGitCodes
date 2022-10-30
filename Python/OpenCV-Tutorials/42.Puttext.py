# Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used.
# bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

# Return Value: It returns an image.

# Python program to explain cv2.putText() method
	
# importing cv2
import cv2
	
# path
path = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
	
# Reading an image in default mode
image = cv2.imread(path)
	
# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 1 px
thickness = 1

# Using cv2.putText() method;(default:False)
image = cv2.putText(image, 'OpenCV', org, font,
				fontScale, color, thickness, cv2.LINE_AA,True)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()