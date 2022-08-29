import cv2
import numpy as np

lena = cv2.imread(r"H:\MyGitCodes\Python\OpenCV\lena.jpg")
lena1 = lena  # shallow copy
lena2 = lena.copy()  # deep copy
lena[10:100, 10:100] = [0, 0, 255]
while True:
    cv2.imshow('lena', lena)
    cv2.imshow('lena1', lena1)
    cv2.imshow('lena2', lena2)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
print(lena.shape)  # (512, 512, 3)
print(lena.shape[2])  # 3
print(lena.size)  # 786432
print(lena.dtype)  # uint8
