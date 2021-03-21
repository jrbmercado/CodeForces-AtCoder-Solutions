# Grab first line
input1 = list(map(int,input().split(" ")))
numPeople = input1[0]
k = input1[1]

# Grab participation counts
input2 = list(map(int,input().split(" ")))

listWithK = [x + k for x in input2]

# Delete participants who are more than 5
finalList = [x for x in listWithK if x <= 5]

lengthOfList = len(finalList)
answer = lengthOfList//3
print(answer)