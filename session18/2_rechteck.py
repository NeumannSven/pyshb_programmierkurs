'''
Created on 24.01.2022

@author: sven
'''
import cv2

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height =int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

h = 300
w = 400
x = (width // 2) - (w // 2)
y = (height // 2) - (h // 2)

while True:
    _, frame = cap.read()
    cv2.imshow('Kamera', frame)
    
    cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255), thickness=2)
    cv2.imshow('Rechteck', frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()