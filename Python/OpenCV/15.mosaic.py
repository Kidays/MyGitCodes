import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV\lena.jpg')
    print(img.shape)
    face = img[230:380, 220:350]  # width,height
    # method1:
    # face1=cv2.resize(face,(8,8))
    # face2=cv2.resize(face1,(130,150))
    # img[230:380,220:350]=face2
    # method2:
    face=face[::10,::10]
    face=np.repeat(face,10,axis=0)
    face=np.repeat(face,10,axis=1)
    img[230:380, 220:350]=face[:150,:130]
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
