import cv2
import numpy as np
if __name__ == '__main__':
    # lena = cv2.imread(r'H:\MyGitCodes\Python\OpenCV\lena.jpg')
    # cv2.imshow('lena',lena[::-1,:,:])#[height,width,color]
    # cv2.imshow('lena',lena[:,::-1,:])#[height,width,color]
    # cv2.imshow('lena', lena[:, :, ::-1])  # same as below
    # cv2.imshow('lena', lena[:, :, [2,1,0]])  # blue
    # lena1=cv2.resize(lena,(256,256))
    # cv2.imshow('lena', lena1[:, :, [0,1,2]]) 
    # lena2=cv2.cvtColor(lena1,code=cv2.COLOR_BGR2GRAY)
    # lena2=cv2.cvtColor(lena1,code=cv2.COLOR_BGR2HSV)
    img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV\RGB.png')
    print(img.shape)
    img1=cv2.resize(img,(540,540))
    lower_blue=np.array([180,200,0])#HSV:Hue(0~360,0-red,120-green,240-blue), Saturation(0~255), Value(0~255)
    upper_blue=np.array([270,255,255])
    mask=cv2.inRange(img1,lower_blue,upper_blue)
    res=cv2.bitwise_and(img1,img1,mask=mask)
    # cv2.imshow('hsv',mask)
    cv2.imshow('hsv',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
