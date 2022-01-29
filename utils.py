def getPathToFile(fName):
 #Used so that the tool can find files in its bundled form
 from os import path
 bundle_dir = path.abspath(path.dirname(__file__))
 return path.join(bundle_dir, fName)