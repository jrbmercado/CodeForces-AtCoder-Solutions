input0 = int(input())
input1 = list(map(int, input().split(" ")))
maxLength = 1
length = 1
for i in range(1, input0):
    if(input1[i] > input1[i-1]):
        length+=1
    else:
        if(maxLength<length):
            maxLength = length
        length = 1
if(maxLength < length):
    maxLength = length
print(maxLength)