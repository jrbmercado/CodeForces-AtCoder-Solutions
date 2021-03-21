numTest = int(input())
answer = []
for i in range(0, numTest):
    length = int(input())
    input1 = list(map(int,input().split(" ")))
    input1.sort()
    flag = False
    for i in range(1, length):
        #print("Testing " + str(input1[i-1]) + " against " + str(input1[i]))
        if(abs(input1[i-1]-input1[i])>1):
            flag = True
            break
    if (flag):
        answer.append("NO")
    else:
        answer.append("YES")
for i in answer:
    print(i)