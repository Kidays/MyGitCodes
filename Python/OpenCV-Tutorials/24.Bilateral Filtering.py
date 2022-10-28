import cv2

# Read the image.
img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeksforgeeks.png')

# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

cv2.imshow('image', img)
cv2.imshow('bilateral', bilateral)			
	
# De-allocate any associated memory usage		
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()	