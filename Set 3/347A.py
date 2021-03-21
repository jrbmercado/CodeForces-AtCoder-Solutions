numOfInts = int(input())
input1 = list(map(int,input().split(" ")))
input1.sort()
input1[0], input1[-1] = input1[-1], input1[0]
answer = ""
for i in range(0, numOfInts):
    answer += str(input1[i])
    if(i<numOfInts-1):
        answer+= " "
print(answer)