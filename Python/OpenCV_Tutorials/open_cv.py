import numpy as numpy
import cv2

#capture device address

cap = cv2.VideoCapture("sd.mp4")

while(True):
    ret, frame = cap.read()
    cv2.imshow("Camera Frame", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Display Frame", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()