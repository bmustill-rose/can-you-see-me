#Various pieces of text used throughout the application


#Initialization messages
initSuccess = "Welcome to Can You See Me. Press enter to check your faces position, p to take a photo or escape to exit."
initFailure = "Can You See Me was unable to detect your webcam. Please make sure it is connected and turned on then run the program again. Exiting."
loadingMessage = "Loading. Please wait..."

#Lookup tables matching percentage positions to strings
yLookup = {
 0: 'Top',
 20: 'Near the top',
 40: 'Middle',
 60: 'Near the bottom',
 80: 'Bottom'
}

xLookup = {
 0: 'left',
 20: 'slightly to the left',
 40: 'middle',
 60: 'slightly to the right',
 80: 'right'
}

#Lookup table for confidence messages
confidenceMessagesLookup = {
 2: 'Low confidence',
 3: 'Very low confidence'
}

#Generate lists of keys based on the above once at runtime to avoid having to do it for every successful detection
yLookupList = list(yLookup.keys())
xLookupList = list(xLookup.keys())
confidenceMessagesLookupList = list(confidenceMessagesLookup.keys())

#Face and photo related messages
noFace = "No face found. Try adjusting the position of your webcam and or checking the light level of your room."
photoTaken = "Photo taken"