length = int(input())
input1 = list(map(int, input().split(" ")))
input1.sort()
total = 0
i=0
j=length-1
while(i<=j):
    total += (input1[i]+input1[j])*(input1[i]+input1[j])
    i+=1
    j-=1
print(total)