from speechlight import speech
import strings
import vision
import maths

def face(frame, faces):
 middleXY = vision.getMiddleXYOfFace(frame, faces[0])
 yKey = maths.getClosest(strings.yLookupList, middleXY['middleY'])
 xKey = maths.getClosest(strings.xLookupList, middleXY['middleX'])
 if strings.yLookup[yKey].lower() == strings.xLookup[xKey].lower():
  utterance = strings.yLookup[yKey]
 else:
  utterance = "{} and {}".format(strings.yLookup[yKey], strings.xLookup[xKey])
 if len(faces) > 1: utterance = utterance + ". "+strings.confidenceMessagesLookup[maths.getClosest(strings.confidenceMessagesLookupList, len(faces))]
 speech.output(utterance)

def noFace():
 speech.output(strings.noFace)

def launchError():
 import sys
 speech.output(strings.initFailure)
 sys.exit(1)

def takePhoto(cv2, frame):
 import datetime
 fName = str(datetime.datetime.now()).replace(':', '-')+'.jpg'
 cv2.imwrite(fName, frame)
 speech.output(strings.photoTaken)