from PIL import Image
import pytesseract
import sys
import os
from PIL import ImageEnhance
os.chdir(sys.path[0])
im = Image.open('www.chemsrc.com_casindex_.png')
# im = Image.open('cas.png')
im = im.convert('L')  # 'RGB'
print(im.size)
# cropped=im.crop((950,410,1899,6500))
# cropped = im.crop((1250, 410, 1899, 6500))
# im = im.crop((1500, 6350, 1899, 6500))  # L,T,R,B
# enhancer = ImageEnhance.Color(im)
# enhancer = enhancer.enhance(0)
# enhancer = ImageEnhance.Brightness(enhancer)
# enhancer = enhancer.enhance(2)
# enhancer = ImageEnhance.Contrast(enhancer)
# enhancer = enhancer.enhance(8)
# enhancer = ImageEnhance.Sharpness(enhancer)
# im = enhancer.enhance(20)
# result=pytesseract.image_to_string(im,lang='chi_sim')
# result=pytesseract.image_to_string(cropped,lang='chi_sim')#chi_tra
result = pytesseract.image_to_string(im, lang='eng')
print(result)
