import cv2
import numpy as np
lena = cv2.imread(r"H:\MyGitCodes\Python\OpenCV\lena.jpg")
origin = cv2.imread(r"H:\MyGitCodes\Python\OpenCV\origin.png")
# origin1 = cv2.resize(origin, (0, 0), fx=512/344, fy=512/324)
origin1 = cv2.resize(origin, (512, 512), interpolation=cv2.INTER_AREA)
# cv2.INTER_NEAREST,cv2.INTER_LINEAR,cv2.INTER_CUBIC
print(lena.shape, origin.shape, origin1.shape)
img = np.ones((512, 512, 3), np.uint8)*50
cv2.imshow('lena', lena)
result = cv2.add(lena, img)
cv2.imshow('result', result)
result2 = cv2.subtract(result, img)
cv2.imshow('result2', result2)
result3 = cv2.addWeighted(lena, 0.7, origin1, 0.3, 20)
cv2.imshow('result3', result3)
lena2 = cv2.flip(lena, 1)  # 0,1,-1
cv2.imshow('lena2', lena2)
cv2.waitKey(0)
