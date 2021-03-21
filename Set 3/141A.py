from collections import Counter

# Get inputs
guestName = input()
nameOfResidenceHost = input()
lettersInPile = input()

# Count each character and put it into a dictionary of letter:count
target = guestName+nameOfResidenceHost 
countTarget = Counter(target)
countLettersInPile = Counter(lettersInPile)

flag = True # Flag to check if difference in letter count, if difference in letter count then cannot form target

# Check if we can create guestName and nameOfResidenceHost out of the letters in pile
for i in set(lettersInPile): # For each unique character in the pile of letters
    #print("Comparing " + str(countTarget[i]) + " with "+ str(countLettersInPile[i]))
    if(countTarget[i] != countLettersInPile[i]):
        flag = False
        break
    del countTarget[i]
    del countLettersInPile[i]

# Check for extra letters after attempting to create guestName and nameOfResidenceHost
if countTarget:
  flag = False
if countLettersInPile:
  flag = False

#print(countTarget)
#print(countLettersInPile)

# Output
if(flag):
    print("YES")
else:
    print("NO")