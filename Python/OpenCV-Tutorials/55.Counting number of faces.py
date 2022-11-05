
# Step 1: Import required libraries
import cv2
import numpy as np
import dlib

# Step 2: Open the default camera to capture faces and use the dlib library to get coordinates.
# (0)in VideoCapture is used to connect your computer's default camera
cap = cv2.VideoCapture(0)
# Get the coordinates
detector = dlib.get_frontal_face_detector()

# Step 3: Count the number of faces
# capture the frames continuously
# convert the frames to grayscale(not necessary)
# take an interator / and initialize it to zero
# each time you get the coordinates to the face structure in the frame,increment the iterator by 1
# plot the box around each detected face along with its face count

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    i = 0
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        i += 1
        cv2.putText(frame, 'face_num'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)
    cv2.imshow('frame', frame)

# Step 4: terminate the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 5: Clear windows
cap.release()
cv2.destroyAllWindows()
