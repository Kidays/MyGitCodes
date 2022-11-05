import cv2
path =r'H:\MyGitCodes\Python\OpenCV-Tutorials\white-dot.png'

# reading the image in grayscale mode
img=cv2.imread(path)
gray = cv2.imread(path, 0)

# threshold
th, threshed = cv2.threshold(gray, 100, 255,
		cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	# displaying the image

# findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST,
					cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 0
s2 = 25
xcnts = []

for cnt in cnts:
	if s1<cv2.contourArea(cnt) <s2:
	    xcnts.append(cnt)

# (w,h)=threshed.shape[:2]
# threshed=cv2.resize(threshed,(h*2,w*2))
# printing output
print("\nDots number: {}".format(len(xcnts)))
# contours can only be displayed if the img is of three channels
cv2.drawContours(img, cnts, -1, (255, 0, 0), 1)
cv2.imshow('image', img)

# wait for a key to be pressed to exit
cv2.waitKey(0)

# close the window
cv2.destroyAllWindows()
