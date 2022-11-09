# from PIL import Image
from paddleocr import PaddleOCR
import cv2
import numpy as np
# import sys
# import os
# os.chdir(sys.path[0])
ocr=PaddleOCR(use_angle_cls=True,lang='en')
path=r'H:\MyGitCodes\Python\Crawler\Anti-spider\plate.jpg'
img=cv2.imread(path,0)
ret, thresh1 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
# Taking a matrix of size 5 as the kernel
kernel = np.ones((3, 3), np.uint8)
# # The first parameter is the original image,
# # kernel is the matrix with which image is
# # convolved and third parameter is the number
# # of iterations, which will determine how much
# # you want to erode/dilate a given image.
# img_dilation = cv2.dilate(thresh1, kernel, iterations=1)
# img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
# # cv2.imshow('img',img_erosion)
# # # De-allocate any associated memory usage
# # if cv2.waitKey(0) & 0xff == 27:
# # 	cv2.destroyAllWindows()

result=ocr.ocr(thresh1,cls=True)
# print(result)
s=''
for text in result:
    print(text[1][0])
    s+=text[1][0]
# .strip():start or end
print(s.replace('.',''))
# result=ocr.ocr(img_erosion)
# print(result)
# from PIL import Image
# import pytesseract
# import sys
# import os
# os.chdir(sys.path[0])
# im = Image.open('www.chemsrc.com_casindex_.png')
# im = im.convert('L')  # 'RGB'
# print(im.size)