def getClosest(myList, myNumber):
 #Taken from https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
 from bisect import bisect_left
 pos = bisect_left(myList, myNumber)
 if pos == 0:
  return myList[0]
 if pos == len(myList):
  return myList[-1]
 before = myList[pos - 1]
 after = myList[pos]
 if after - myNumber < myNumber - before:
  return after
 else:
  return before

def isPercentageOf(a, b):
 #a = x% of b
 return (100/b) * a

def middleOf(a, b):
 return (a+b) / 2