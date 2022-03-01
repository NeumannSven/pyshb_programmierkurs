'''
Created on 24.01.2022

@author: sven
'''

import cv2
import time

face_retangle_stack = []

cap = cv2.VideoCapture('videos/IGS Oyten3.mp4')

if cap.isOpened() == False:
    print('Error: Viedeo konnte nicht geladen werden!')

facedect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facedect_profil = cv2.CascadeClassifier('haarcascade_profileface.xml')

def detect_face(frame):

    frame2 = frame.copy()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    for face_rectangle in face_retangle_stack:
        for (x, y, w, h) in face_rectangle:
            face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
            frame2[y:y+h, x:x+w] = face_blur

    face_rectangle = facedect.detectMultiScale(frame_gray, minNeighbors=3, scaleFactor=1.1, minSize=(150,150), maxSize=(800,800))
    face_retangle_stack.append(face_rectangle)
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame2[y:y+h, x:x+w] = face_blur

    face_rectangle = facedect_profil.detectMultiScale(frame_gray, minNeighbors=3, scaleFactor=1.1, minSize=(150,150), maxSize=(800,800))
    face_retangle_stack.append(face_rectangle)
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame2[y:y+h, x:x+w] = face_blur
    
    if len(face_retangle_stack) >= 40:
        del(face_retangle_stack[0:2])
 
    return frame2, frame_gray 


while True:
    ret, frame = cap.read()

    if ret == True:

        frame, frame_gray = detect_face(frame)
        cv2.imshow('Video', frame)
        cv2.imshow('Grau', frame_gray)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()