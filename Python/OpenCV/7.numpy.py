import numpy as np
import cv2
# creatmat
# array() zeros() ones() full() identity/eye()
a = np.array([2, 3, 4])
c = np.array([[1, 2], [3, 4]])
# print(a,c)
d = np.zeros((480, 640, 3), np.uint8)
# print(d)
e = np.full((480, 640, 3), 128, np.uint8)
# print(e)
f = np.identity(8)
print(f)
g = np.eye(5, 8, k=2)
print(g)
# [[0. 0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]]
# [y,x]
print(d[100, 100])
count = 0
while count < 200:
    d[count, count+100, 2] = 255
    # d[count,count+100]=[0,0,255]
    count += 1
roi = d[100:200, 100:200]
roi[:, :] = [0, 0, 255]
cv2.imshow('img', d)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
# [y1:y2,x1:x2]
# [:,:]
