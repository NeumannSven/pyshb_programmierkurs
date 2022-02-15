'''
Created on 24.01.2022

@author: sven
'''

import cv2
import time

cap = cv2.VideoCapture('video.mp4')

if cap.isOpened() == False:
    print('Error: Viedeo konnte nicht geladen werden!')

facedect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(frame):
    face_rectangle = facedect.detectMultiScale(frame)
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame[y:y+h, x:x+w] = face_blur
    return frame 

while True:
    ret, frame = cap.read()

    if ret == True:

        frame = detect_face(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()