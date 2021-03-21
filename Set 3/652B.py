length = int(input())
input1 = list(map(int,input().split(" ")))
input1.sort(reverse=True)
i = 0
j = 1
answer = [0]*length
while(j<length):
    answer[j]=input1[i]
    i+=1
    j+=2
j=0
while(j<length):
    answer[j]=input1[i]
    i+=1
    j+=2
for i in range(0, len(answer)):
    print(answer[i], end=" ")