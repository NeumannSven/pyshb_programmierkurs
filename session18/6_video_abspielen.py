'''
Created on 24.01.2022

@author: sven
'''

import cv2
import time

cap = cv2.VideoCapture('video.mp4')

if cap.isOpened() == False:
    print('Error: Viedeo konnte nicht geladen werden!')

while True:
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('Video', frame)
        time.sleep(1/30)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()