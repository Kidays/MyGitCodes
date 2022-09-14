from imutils import countours
import numpy as np
import argparse
import imutils
import cv2
import myutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
ap.add_argument("-t","--template",required=True,help="path to template OCR-A image")
args=vars(ap.parse_args())
FIRST_NUMBER={
    "3":"American Express",
    "4":"Visa",
    "5":"MasterCard",
    "6":"Discover Card"
}
