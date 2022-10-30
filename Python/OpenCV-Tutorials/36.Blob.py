import cv2
import numpy as np

# Load image,"0":cv2.IMREAD_GRAYSCALE
image = cv2.imread(r'H:\MyGitCodes\Python\OpenCV-Tutorials\blob.png', 0)

image = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                           cv2.BORDER_CONSTANT, None, value=(255, 255, 255))

# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying Otsu thresholding
# as an extra flag in binary
# thresholding
ret, thresh1 = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(thresh1, -1, kernel)

# Set our filtering parameters
# Initialize parameter setting using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 800

# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.89

# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.95

# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.9

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(dst)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (255, 0, 0),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
print(text)
# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
