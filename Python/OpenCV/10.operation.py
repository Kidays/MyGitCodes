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
lena3 = cv2.rotate(lena, cv2.ROTATE_90_CLOCKWISE)
# cv2.ROTATE_90_COUNTERCLOCKWISE,cv2.ROTATE_180
cv2.imshow('lena3', lena3)
h, w, ch = lena.shape
M = np.float32([[1, 0, 200], [0, 1, 100]])
lena4 = cv2.warpAffine(lena, M, (w, h))
cv2.imshow('lena4', lena4)
M = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.5)  # center,angle,scale
lena5 = cv2.warpAffine(lena, M, (w, h))
cv2.imshow('lena4', lena5)
src=np.float32([[100,150],[300,350],[150,280]])
dst=np.float32([[120,180],[330,380],[160,300]])
M=cv2.getAffineTransform(src,dst)
lena6=cv2.warpAffine(lena,M,(w,h))
cv2.imshow('lena6',lena6)
cv2.waitKey(0)