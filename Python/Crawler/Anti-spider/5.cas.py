import cv2
import csv
# not the top position;TypeError: 'NoneType' object is not subscriptable
from paddleocr import PaddleOCR
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
# img = im[328:428, 450:740]  # [TOP:BOTTOM,LEFT:RIGHT]
# img = im[5130:5228, 450:740]  
# img=im[1823:1934,180:390]
# img=im[380:2000,0:180]
# result = ocr.ocr(img, cls=True)
# for text in result:
#     print(text[1][0])
# cv2.imshow('crop', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
for i in range(50):
    h1 = int(328+int(i*97.5))
    h2 = int(h1+97.5)
    # cv2.line(im,(450,h1),(740,h1),(0,0,255),5)
    img = im[h1:h2, 450:740]  # [TOP:BOTTOM,LEFT:RIGHT]
    result = ocr.ocr(img, cls=True)
    # print(len(result))
    # result:[[[0], ('2.4-Bis(q.g-diMethylbenzyI)phe', 0.86897224)], [[[8.0, 59.0], [27.0, 59.0], [27.0, 73.0], [8.0, 73.0]], ('nol', 0.96516514)]]
    s = ''
    for j in range(len(result)):
        # print(result[j][1][0])
        s += str(result[j][1][0])
    # print(s)
    with open('cas.csv', 'a+', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([s])
        # w.writerow(["abcdef"])
        # w.writerow("abcdef")

# h=im.shape[0]-174
# img=im[h:im.shape[0],0:800]
# cv2.imshow('crop',im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
