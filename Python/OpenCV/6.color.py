import cv2


def callback():
    pass


cv2.namedWindow('color', cv2.WINDOW_NORMAL)
# img = cv2.imread('./lena.jpg')
img=cv2.imread(r"H:\MyGitCodes\Python\OpenCV\lena.jpg")
colorspaces = [cv2.COLOR_BGRA2RGBA, cv2.COLOR_BGR2BGRA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2YUV, cv2.COLOR_RGB2HSV_FULL]
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces), callback)
while True:
    index = cv2.getTrackbarPos('curcolor', 'color')
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
