import maths
import strings
import vision

def generateSimpleFaceLocationUtterance(frame, faces):
 middleXY = vision.getMiddleXYOfFace(frame, faces[0])
 yKey = maths.getClosest(strings.yLookupList, middleXY['middleY'])
 xKey = maths.getClosest(strings.xLookupList, middleXY['middleX'])
 if strings.yLookup[yKey].lower() == strings.xLookup[xKey].lower():
  utterance = strings.yLookup[yKey]+"."
 else:
  utterance = strings.simpleFaceLocation.format(strings.yLookup[yKey], strings.xLookup[xKey])
 if len(faces) > 1: utterance = utterance + strings.confidenceMessagesLookup[maths.getClosest(strings.confidenceMessagesLookupList, len(faces))]
 return utterance

def generateDetailedFaceLocationUtterance(frame, faces):
 middleXY = vision.getMiddleXYOfFace(frame, faces[0])
 return strings.detailedFaceLocation.format(round(middleXY['middleY'], 1), round(middleXY['middleX'], 1))

def generateNoFaceUtterance():
 return strings.noFacesFound

def generateDebugUtterance(faces):
 utterance = strings.debugIntro.format(str(len(faces)))
 for (x,y,w,h) in faces:
  utterance = utterance + strings.debugFaceInfo.format(x, y, w, h)
 return utterance