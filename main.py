from multiprocessing.connection import wait
import cv2
from cv2 import imshow
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while (1):
    success, img = cap.read()
    imshow("test", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
