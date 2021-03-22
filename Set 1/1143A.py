numOfDoors = int(input())
sample = input().split(" ")
totalDoorsLeft = 0
totalDoorsRight = 0
for i in range(0, numOfDoors):
    if(sample[i]=="0"):
        totalDoorsLeft+=1
    if(sample[i]=="1"):
        totalDoorsRight+=1
for i in range(0, numOfDoors):
    if(sample[i]=="0"):
        totalDoorsLeft-=1
    if(sample[i]=="1"):
        totalDoorsRight-=1
    if(totalDoorsLeft==0 or totalDoorsRight==0):
        print(i+1)
        break