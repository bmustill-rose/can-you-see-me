from speechlight import speech
import cv2

import strings
import handlers

speech.output(strings.loadingMessage)
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#VideoCapture won't throw an exception if the device doesn't exist so only cv2-native way of figuring out if a webcam is attached is to try and display an image from it and see what happens
try:
 ret, frame = cap.read()
 cv2.imshow(strings.initSuccess, frame)
except:
 handlers.launchError()

while True:
 ret, frame = cap.read()
 faces = faceCascade.detectMultiScale(frame)
 if len(faces) > 0:
  for (x, y, w, h) in faces:
   cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
 cv2.imshow(strings.initSuccess, frame)
 c = cv2.waitKey(1)
 if c == 27: break
 elif c == 112: handlers.takePhoto(cv2, frame)
 elif c == 13:
  if len(faces) > 0:
   handlers.face(frame, faces)
  else:
   handlers.noFace()

cap.release()
cv2.destroyAllWindows()