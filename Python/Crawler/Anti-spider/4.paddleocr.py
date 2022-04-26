from PIL import Image
from paddleocr import PaddleOCR
import sys
import os
os.chdir(sys.path[0])
ocr=PaddleOCR(use_angle_cls=True,lang='en')
path=r'H:\MyGitCodes\Python\Crawler\Anti-spider\test.png'
result=ocr.ocr(path,cls=True)
for text in result:
    print(text)
# result=ocr.ocr(im)
# print(result)
# from PIL import Image
# import pytesseract
# import sys
# import os
# os.chdir(sys.path[0])
# im = Image.open('www.chemsrc.com_casindex_.png')
# im = im.convert('L')  # 'RGB'
# print(im.size)