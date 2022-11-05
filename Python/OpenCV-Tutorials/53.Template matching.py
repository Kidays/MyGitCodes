# Python program to illustrate
# template matching
# template matching is not suitable for processing multiple tests
import cv2
import numpy as np

# Read the main image
img_rgb = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\array.jpg')

# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Read the template
template = cv2.imread(
    r'H:\MyGitCodes\Python\OpenCV-Tutorials\array-dot.jpg', 0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Perform match operations.
# cv2.TM_SQDIFF ------平方差匹配法(最好匹配0)
# cv2.TM_SQDIFF_NORMED ------归一化平方差匹配法(最好匹配0)
# cv2.TM_CCORR ------相关匹配法(最坏匹配0)
# cv2.TM_CCORR_NORMED ------归一化相关匹配法(最坏匹配0)
# cv2.TM_CCOEFF ------系数匹配法(最好匹配1)
# cv2.TM_CCOEFF_NORMED ------化相关系数匹配法(最好匹配1)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.82

# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw a rectangle around the matched region.
# zip([iterable, ...])
i = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
    i += 1

# Show the final image with the matched area.
print(i)
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
