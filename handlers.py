from speechlight import speech

import generators
import strings
import vision

def scanForFaces(cv2, faceCascade, frame, key):
 faces = faceCascade.detectMultiScale(frame, minNeighbors=6, minSize=(60,60), scaleFactor=1.1)
 if len(faces) > 0:
  faces = vision.sortFacesLargeToSmall(faces)
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