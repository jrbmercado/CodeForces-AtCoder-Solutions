input1 = list(map(int,input().split()))
track1 = list(map(int,input().split()))
track2 = list(map(int,input().split()))
numStations = input1[0]
targetIndex = input1[1]-1
flag = False
lastStationTransfer = 0

for i in range(0, numStations):
    if(track1[i] == 1):
        if(i==targetIndex):
            flag = True
            break
        
for i in range(0, numStations):
    if(track1[i]==1 and track2[i]==1):
        lastStationTransfer = max(lastStationTransfer,i)
        
if(not flag):
    for i in range(lastStationTransfer, 0, -1):
        if(track2[i] == 1):
            if(i==targetIndex):
                flag = True
                break
            
if(track1[0]==0):
    flag=False
    
if(flag):
    print("YES")
else:
    print("NO")