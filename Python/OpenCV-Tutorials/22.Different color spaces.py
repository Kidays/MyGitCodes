# Python program to read image as RGB

# Importing cv2 and matplotlib module
import cv2
import matplotlib.pyplot as plt

# reads image as RGB
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeksforgeeks.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# shows the image
plt.imshow(laplacian)
plt.show()