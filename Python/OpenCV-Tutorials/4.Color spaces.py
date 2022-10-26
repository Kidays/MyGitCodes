import cv2

image = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\geeksforgeeks.png')
B, G, R = cv2.split(image)
# Corresponding channels are separated

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
