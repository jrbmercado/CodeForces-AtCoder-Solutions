numTestCases = int(input())
arrLengths = []
arrTests = []
for i in range(0, numTestCases):
    arrLengths.append(int(input()))
    input1 = list(map(int,input().split(" ")))
    arrTests.append(input1)

for i in range(0, numTestCases):
    flag = 1
    lengthPass = arrLengths[i]
    password = arrTests[i]
    x = password[0]
    for i in range(1, lengthPass):
        if(x!=password[i]):
            flag=0
    if(flag):
        print(lengthPass)
    else:
        print("1")