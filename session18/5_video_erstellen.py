'''
Created on 24.01.2022

@author: sven
'''

import cv2

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while True:
    _, frame = cap.read()
    
    cv2.imshow('Kamera 1', frame)
    
    writer.write(frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()