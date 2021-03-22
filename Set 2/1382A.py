numTestCases = int(input())
listOfArr1Lengths = []
listOfArr2Lengths = []
listOfArr1s = []
listOfArr2s = []
for i in range(0, numTestCases):
    input1 = list(map(int, input().split(" ")))
    listOfArr1Lengths.append(input1[0])
    listOfArr2Lengths.append(input1[1])
    input2 = list(map(int, input().split(" ")))
    listOfArr1s.append(input2)
    input3 = list(map(int, input().split(" ")))
    listOfArr2s.append(input3)

for i in range(0, numTestCases):
    lenOfArr1 = listOfArr1Lengths[i]
    lenOfArr2 = listOfArr2Lengths[i]
    arr1 = listOfArr1s[i]
    arr2 = listOfArr2s[i]

    set1 = set(arr1)
    set2 = set(arr2)
    answer = set(set1).intersection(set2)
    if(len(answer)==0):
        print("NO")
    else:
        var1 = answer.pop()
        print("YES")
        print("1" + " " + str(var1))