#Various pieces of text used throughout the application

#Initialization and argument related messages
initSuccess = "Welcome to Can You See Me. Press enter to check your faces position, d for more detailed information, p to take a photo or escape to exit."
initFailure = "Can You See Me was unable to detect your webcam. Please make sure it is connected and turned on then run the program again. Exiting."
loadingMessage = "Loading. Please wait..."
debugDescription = "Draw outlines around all detected faces"

#Lookup tables matching percentage positions to strings
yLookup = {
 10: 'Top',
 30: 'Near the top',
 50: 'Middle',
 70: 'Near the bottom',
 90: 'Bottom'
}

xLookup = {
 10: 'left',
 30: 'slightly to the left',
 50: 'middle',
 70: 'slightly to the right',
 90: 'right'
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
detailedFaceLocation = " X: {}%, Y: {}%."
noFacesFound = "No face found. Try adjusting the position of your webcam and or checking the light level of your room."
photoTaken = "Photo taken"
debugIntro = " {} faces found."
debugFaceInfo = " X: {}, Y: {}, width: {}, height: {}."