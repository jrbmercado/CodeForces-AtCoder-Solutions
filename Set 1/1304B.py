def checkPalindromeSelf(word):
    return word == word[::-1]
    
input1 = input().split(" ")
numStrings = int(input1[0])
lenStrings = int(input1[1])
myArray = []

for i in range(0, numStrings):
    temp = input()
    #print("appending "+ temp)
    myArray.append(temp)
#print(myArray)

left = ""
right = ""
middle = ""

for i in range(0, numStrings):
    reversedWord = myArray[i][::-1]
    if(reversedWord == myArray[i]):
        #print("palindrome self, putting in middle")
        middle=myArray[i]
        #print("middle: " + middle)
    else:
        #print("not palindrom self")
        for j in range(i+1, numStrings):
            #print("checking for " + str(reversedWord) + " = " + str(myArray[j]))
            if(reversedWord == myArray[j]):
                #print("palindrome pair found")
                left+=myArray[i]
                right= reversedWord + right
                #print("left: " + left)
                #print("right: " + right)
                break
answer = left+middle+right
print(len(answer))
print(answer)