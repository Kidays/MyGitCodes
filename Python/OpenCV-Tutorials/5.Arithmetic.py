# # Python program to illustrate
# # arithmetic operation of
# # addition of two images
# import cv2
# import numpy as np
# # organizing imports

# # path to input images are specified and
# # images are loaded with imread command
# image1 = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\input1.jpg')
# image2 = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\input2.jpg')
# # cv2.addWeighted is applied over the
# # image inputs with applied parameters
# # print(image1.shape)
# # print(image2.shape)
# weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# # the window showing output image
# # with the weighted sum
# cv2.imshow('Weighted Image', weightedSum)

# # De-allocate any associated memory usage
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ___________________________________________________

# Python program to illustrate
# arithmetic operation of
# subtraction of pixels of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\rec.png')
image2 = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\dot.png')

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the subtracted image
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
