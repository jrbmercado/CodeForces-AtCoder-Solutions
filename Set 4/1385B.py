from collections import Counter
numTestCases = int(input())
lengthArray = []
dataArray = []
for i in range(0, numTestCases):
    lengthArray.append(int(input()))
    dataArray.append(list(map(int,input().split(" "))))
for i in range(0, numTestCases):
    output = ""
    counterObj = Counter(dataArray[i])
    for key in counterObj.keys():
        print(key, end=" ")
   