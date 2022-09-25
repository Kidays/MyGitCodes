import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread(r'H:\MyGitCodes\Python\OpenCV\Multi_faces.png')
    gray=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(
        r'H:\MyGitCodes\Python\OpenCV\haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.24,minNeighbors=1,minSize=(25,25))
    print(faces)  # [[217 201 173 173]]
    for x,y,w,h in faces:
        cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=[255,0,0],thickness=2)
    cv2.imshow('lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
