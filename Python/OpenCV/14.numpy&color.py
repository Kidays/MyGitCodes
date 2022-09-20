import cv2
import numpy as np
if __name__ == '__main__':
    lena = cv2.imread(r'H:\MyGitCodes\Python\OpenCV\lena.jpg')
    # cv2.imshow('lena',lena[::-1,:,:])#[height,width,color]
    # cv2.imshow('lena',lena[:,::-1,:])#[height,width,color]
    # cv2.imshow('lena', lena[:, :, ::-1])  # same as below
    # cv2.imshow('lena', lena[:, :, [2,1,0]])  # blue
    cv2.imshow('lena', lena[:, :, [0,1,2]])  # blue
    cv2.waitKey(0)
    cv2.destroyAllWindows()
