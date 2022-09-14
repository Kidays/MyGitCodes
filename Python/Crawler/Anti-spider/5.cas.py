import cv2
from paddleocr import PaddleOCR # not the top position;TypeError: 'NoneType' object is not subscriptable
# import sys
# import os
# import numpy as np
# from PIL import Image
# from PIL import ImageEnhance
# os.chdir(sys.path[0])#contains paddleocr sys variables
# # path=r'H:\MyGitCodes\Python\Crawler\Anti-spider\www.chemsrc.com_casindex_.png'
# # result=ocr.ocr(path,cls=True)
# # # print(result)
# im = Image.open('image1.png')
# im = im.convert('L')  # 'RGB' ;L = R * 299/1000 + G * 587/1000+ B * 114/1000
# print(im.size)
# `ch`, `en`, `french`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang='ch')
# im = im.crop((0, 330, 799, 800))  # L,T,R,B
# im=np.array(im).astype('uint8')*255
# img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
im = cv2.imread(r'H:\MyGitCodes\Python\Crawler\Anti-spider\image1.png')
print(im.shape)
# img = im[180:330, 0:800]  # [TOP:BOTTOM,LEFT:RIGHT]
# img=im[330:360,0:800]
# img=im[380:2000,0:180]
# result = ocr.ocr(img, cls=True)
# for text in result:
#     print(text[1][0])
# cv2.imshow('crop', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
for i in range(50):
    h1=int(380+i*111)
    h2=int(h1+111.2)
    img=im[h1:h2,180:390]
    result = ocr.ocr(img, cls=True)
    for text in result:
        print(text[1][0])
# h=im.shape[0]-174
# img=im[h:im.shape[0],0:800]
# cv2.imshow('crop',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()