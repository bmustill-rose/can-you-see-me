from speechlight import speech

import generators
import strings
import vision

def scanForFaces(faceCascade, frame, key):
 faces = vision.findFaces(faceCascade, frame)
 if len(faces) > 0:
  utterance = generators.generateSimpleFaceLocationUtterance(frame, faces)
  if key == 100: utterance = utterance + generators.generateDetailedFaceLocationUtterance(frame, faces)
 else:
  utterance = generators.generateNoFaceUtterance()
 speech.output(utterance)

def launchError():
 import sys
 speech.output(strings.initFailure)
 sys.exit(1)

def takePhoto(cv2, frame):
 import datetime
 fName = str(datetime.datetime.now()).replace(':', '-')+'.jpg'
 cv2.imwrite(fName, frame)
 speech.output(strings.photoTaken)

def debug(cv2, faceCascade, frame):
 faces = vision.findFaces(faceCascade, frame)
 for (x,y,w,h) in faces:
  cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)