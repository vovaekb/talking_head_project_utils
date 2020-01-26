import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
    help="path to input video file")
args = vars(ap.parse_args())

print('File: ', args['file'])

cap = cv2.VideoCapture(args['file']) # 'fake.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    try:
        cv2.imshow('frame',frame)
    except:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
