# Verpixeln von Gesichtern mit OpenCV


## installion

``` shell
sudo pip3 install opencv-python
```

## Gesicheter aus Kamera verpixeln

### Kamerabild anzeigen

``` python
import cv2

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    cv2.imshow('Kamera 1', frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
```

### Auf Kamerabild zeichnen 

``` python
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
```
### Kamera Ausschnitt verpixeln 

``` python
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
```

### Gesicht im Kamerabild suchen und verpixeln 

``` python
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
```




## Gesichter im Video verpixeln
