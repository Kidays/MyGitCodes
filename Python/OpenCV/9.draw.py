import cv2
import numpy as np
# img = np.zeros((480, 640, 3), np.uint8)  # (y,x,c)
# cv2.line(img, (10, 20), (600, 400), (0, 0, 255),2,16)  # (img,(x1,y1),(x2,y2),(b,g,r),thickness,li
# #linetype:-1,4,8,16
# cv2.line(img, (50, 400), (600, 100), (0, 255, 255),5,-1)
# cv2.rectangle(img,(10,10),(100,100),(0,0,255),-1)
# cv2.circle(img,(320,320),50,(0,0,255))
# cv2.ellipse(img,(240,120),(100,50),0,0,120,(0,0,255))
# pts=np.array([(300,10),(150,50),(400,100)],np.int32)
# cv2.polylines(img,[pts],True,(0,0,255))
# cv2.fillPoly(img,[pts*2],(255,255,0))
# cv2.putText(img,'NIHAO!',(200,200),4,2,(255,255,0),0)
# cv2.imshow('img', img)
# cv2.waitKey(0)
img = np.zeros((480, 640, 3), np.uint8)
curshape = 0
startpos = (0, 0)


def mouse_callback(event, x, y, flags, userdata):
    global curshape, startpos
    # print(event, x, y, flags, userdata)
    if(event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x, y)
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if curshape == 1:
            cv2.line(img, startpos, (x, y), (0, 0, 255))
        elif curshape == 2:
            cv2.rectangle(img, startpos, (x, y), (0, 0, 255))
        elif curshape == 3:
            a = (x-startpos[0])
            b = (y-startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos, r, (0, 0, 255))
        else:
            print('error:no shape')


cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('drawshape', mouse_callback)
while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):
        curshape = 1
    elif key == ord('r'):
        curshape = 2
    elif key == ord('c'):
        curshape = 3
cv2.destroyAllWindows()
