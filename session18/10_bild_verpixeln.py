'''
Created on 01.03.2022

@author: sven
'''

import cv2

img = cv2.imread('videos/solvay_conference.jpg')

facedect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facedect_profil = cv2.CascadeClassifier('haarcascade_profileface.xml')

def detect_face(frame):

    frame2 = frame.copy()

    face_rectangle = facedect.detectMultiScale(frame, minNeighbors=5, scaleFactor=1.1, minSize=(50,80))
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame2[y:y+h, x:x+w] = face_blur
    
    face_rectangle = facedect_profil.detectMultiScale(frame, minNeighbors=3, scaleFactor=1.1, minSize=(50,80))
    for (x, y, w, h) in face_rectangle:
        face_blur = cv2.blur(frame[y:y+h, x:x+w], (50,50))
        frame2[y:y+h, x:x+w] = face_blur
    
    return frame2 


frame = detect_face(img)
cv2.imshow('Bild 1', frame)


cv2.waitKey()
    

