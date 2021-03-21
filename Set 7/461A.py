length = int(input())
input1 = list(map(int, input().split(" ")))
score = sum(input1)
possibleGroups = score
x = length-1
input1.sort()
k = 0
while(k!=x):
    score+=input1[k]
    possibleGroups-=input1[k]
    score+=possibleGroups
    k+=1
print(score)