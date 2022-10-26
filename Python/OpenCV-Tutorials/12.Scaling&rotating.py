import cv2
import numpy as np

FILE_NAME = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Get number of pixel horizontally and vertically.
	(height, width) = img.shape[:2]

	# Specify the size of image along with interpolation methods.
	# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
	# is used for zooming.
	res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

	# Write image back to disk.
	cv2.imwrite('result.jpg', res)

except IOError:
	print ('Error while reading files !!!')

#__________________________________________________
import cv2
import numpy as np

FILE_NAME =  r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
try:
	# Read image from the disk.
	img = cv2.imread(FILE_NAME)

	# Shape of image in terms of pixels.
	(rows, cols) = img.shape[:2]

	# getRotationMatrix2D creates a matrix needed for transformation.
	# We want matrix for rotation w.r.t center to 45 degree without scaling.
	M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
	res = cv2.warpAffine(img, M, (cols, rows))

	# Write image back to disk.
	cv2.imwrite('result.jpg', res)
except IOError:
	print ('Error while reading files !!!')

#__________________________________________________
import cv2
import numpy as np

FILE_NAME = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#	 [0 1 y]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

try:

	# Read image from disk.
	img = cv2.imread(FILE_NAME)
	(rows, cols) = img.shape[:2]

	# warpAffine does appropriate shifting given the
	# translation matrix.
	res = cv2.warpAffine(img, M, (cols, rows))

	# Write image back to disk.
	cv2.imwrite('result.jpg', res)

except IOError:
	print ('Error while reading files !!!')

#____________________________________________________

import cv2
import numpy as np

FILE_NAME = r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeks.png'
try:
	# Read image from disk.
	img = cv2.imread(FILE_NAME)

	# Canny edge detection.
	edges = cv2.Canny(img, 100, 200)

	# Write image back to disk.
	cv2.imwrite('result.jpg', edges)
except IOError:
	print ('Error while reading files !!!')

