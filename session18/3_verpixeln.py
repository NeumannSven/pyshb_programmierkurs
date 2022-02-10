'''
Created on 24.01.2022

@author: sven
'''

import cv2

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height =int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width // 2;
y = height // 2;

while True:
    _, frame = cap.read()
    
    cv2.imshow('Kamera', frame)
    
    blur_frame = cv2.blur(frame, (50,50))
    
    blur_frame = blur_frame[y:y+300, x:x+400]
    
            
    cv2.imshow('Verpixelt', blur_frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()