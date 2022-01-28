import maths
import strings
import vision

def generateSimpleFaceLocationUtterance(frame, faces):
 middleXY = vision.getMiddleXYOfFace(frame, faces[0])
 yKey = maths.getClosest(strings.yLookupList, middleXY['middleY'])
 xKey = maths.getClosest(strings.xLookupList, middleXY['middleX'])
 if strings.yLookup[yKey].lower() == strings.xLookup[xKey].lower():
  utterance = strings.yLookup[yKey]
 else:
  utterance = "{} and {}".format(strings.yLookup[yKey], strings.xLookup[xKey])
 if len(faces) > 1: utterance = utterance + ". "+strings.confidenceMessagesLookup[maths.getClosest(strings.confidenceMessagesLookupList, len(faces))]
 return utterance

def generateDetailedFaceLocationUtterance(frame, faces):
 middleXY = vision.getMiddleXYOfFace(frame, faces[0])
 return ". x: {}% y: {}%".format(round(middleXY['middleX'], 1), round(middleXY['middleY'], 1))

def generateNoFaceUtterance():
 return strings.noFace
