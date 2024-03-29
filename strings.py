#Various pieces of text used throughout the application

#Initialization and argument related messages
initSuccess = "Welcome to Can You See Me. Press enter to check your faces position, d for more detailed information, p to take a photo or escape to exit."
initFailure = "Can You See Me was unable to detect your webcam. Please make sure it is connected and turned on then run the program again. Exiting."
loadingMessage = "Loading. Please wait..."
debugDescription = "Draw outlines around all detected faces"

#Lookup tables matching percentage positions to strings
yLookup = {
 25: 'At the top',
 35: 'Towards the top',
 45: 'Slightly towards the top',
 50: 'In the middle',
 55: 'Slightly towards the bottom', 
 65: 'Towards the bottom',
 75: 'At the bottom'
}

xLookup = {
 25: 'to the right',
 35: 'approaching the right',
 45: 'slightly to the right',
 50: 'in the middle',
 55: 'slightly to the left',
 65: 'approaching the left',
 75: 'to the left'
}

#Lookup table for confidence messages
confidenceMessagesLookup = {
 2: ' Low confidence.',
 3: ' Very low confidence.'
}

#Generate lists of keys based on the above once at runtime to avoid having to do it for every successful detection
yLookupList = list(yLookup.keys())
xLookupList = list(xLookup.keys())
confidenceMessagesLookupList = list(confidenceMessagesLookup.keys())

#Face, photo and debugging related messages
simpleFaceLocation = "{} and {}."
detailedFaceLocation = " Y: {}%, X: {}%."
noFacesFound = "No face found. Try adjusting the position of your webcam and or checking the light level of your room."
photoTaken = "Photo taken"
debugIntro = " {} faces found."
debugFaceInfo = " X: {}, Y: {}, width: {}, height: {}."