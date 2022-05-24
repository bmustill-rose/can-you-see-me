#from re import X
import maths

def findFaces(faceCascade, frame):
 faces = faceCascade.detectMultiScale(frame, minNeighbors=6, minSize=(60,60), scaleFactor=1.1)
 if len(faces) > 0:
  faces = sortFacesLargeToSmall(faces)
 return faces

def getImageXY(frame):
 y, x, c = frame.shape
 return {'x': x, 'y': y}

def getMiddleXYOfFace(frame, face):
 #Returns the percentage of the middle xy of the face in relation to xy of the frame
 frameXY = getImageXY(frame)
 xPercentage = maths.isPercentageOf(maths.middleOf(face[0], face[0]+face[2]), frameXY['x'])
 yPercentage = maths.isPercentageOf(maths.middleOf(face[1], face[1]+face[3]), frameXY['y'])
 return {'middleX': xPercentage, 'middleY': yPercentage}

def sortFacesLargeToSmall(faces):
 #Returns a list of tuples where the order of the tuples has been sorted by adding the third and fourth values of each tuple together - E.G. the w& h of a face
 return sorted(faces, key=lambda x: x[2]+x[3], reverse=True)