'''
Created on 27.01.2022

@author: sven
'''
import cv2

cap = cv2.VideoCapture(1)
facedect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(frame):
    face_rectangle = facedect.detectMultiScale(frame)
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame[y:y+h, x:x+w] = face_blur
    return frame 

while True:
    _, frame = cap.read()
    frame = detect_face(frame)
    cv2.imshow('Verpixelt', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()