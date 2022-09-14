import cv2
import numpy as np
img = cv2.imread(r"H:\MyGitCodes\Python\OpenCV\lena.jpg")
kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('lena', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
