import cv2
from speechlight import speech

import handlers
import strings
import utils

speech.output(strings.loadingMessage)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) #Attempt to set webcam resolution to 1080P. Will / should gracefully fall back to maximum supported if it can't

faceCascade = cv2.CascadeClassifier(utils.getPathToFile('haarcascade_frontalface_default.xml'))

#VideoCapture won't throw an exception if the device doesn't exist so only cv2-native way of figuring out if a webcam is attached is to try and display an image from it and see what happens
try:
 ret, frame = cap.read()
 cv2.imshow(strings.initSuccess, frame)
except:
 handlers.launchError()

while True:
 ret, frame = cap.read()
 cv2.imshow(strings.initSuccess, frame)
 key = cv2.waitKey(1)
 if key == 27: break
 elif key == 112: handlers.takePhoto(cv2, frame)
 elif key == 13 or key == 100: handlers.scanForFaces(cv2, faceCascade, frame, key)

cap.release()
cv2.destroyAllWindows()