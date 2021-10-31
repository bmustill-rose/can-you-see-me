import maths

def getImageXY(frame):
 x, y, c = frame.shape
 return {'x': x, 'y': y}

def getMiddleXYOfFace(frame, face):
 #Returns the percentage of the middle xy of the face in relation to xy of the frame
 frameXY = getImageXY(frame)
 xPercentage = maths.isPercentageOf(maths.middleOf(face[0], face[2]), frameXY['x'])
 yPercentage = maths.isPercentageOf(maths.middleOf(face[1], face[3]), frameXY['y'])
 return {'middleX': xPercentage, 'middleY': yPercentage}