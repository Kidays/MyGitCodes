# # import opencv
# import cv2

# # Load the input image
# image = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png')
# cv2.imshow('Original', image)
# cv2.waitKey(0)

# # Use the cvtColor() function to grayscale the image
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)

# # Window shown waits for any key pressing event
# cv2.destroyAllWindows()

#_____________________________________________________
# Import opencv
import cv2

# Use the second argument or (flag value) zero
# that specifies the image is to be read in grayscale mode
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png',0)

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()

#_____________________________________________________
# Import opencv
import cv2

# Load the input image
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png')

# Obtain the dimensions of the image array
# using the shape method
(row, col) = img.shape[0:2]

# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
	for j in range(col):
		# Find the average of the BGR pixel values
		img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()

