#capturing image from webcam

import cv2
cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:    # frame captured without any errors
     cv2.imwrite("sandeep.jpg",img)
cam.release()
