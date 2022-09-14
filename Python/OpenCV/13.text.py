import numpy as np
import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image to be scanned")
args=vars(ap.parse_args())
def order_points(pts):
    rect=np.zeros((4,2),type="float32")
    s=pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff=np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]
    return rect
