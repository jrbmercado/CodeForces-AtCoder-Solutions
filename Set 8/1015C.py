input1 = list(map(int, input().split(" ")))
numSongs = input1[0]
maximum = input1[1]
uncompressed = []
compressed = []
difference = []
sumCompressed = 0
for i in range(0, numSongs):
    input2 = list(map(int, input().split(" ")))
    uncompressed.append(input2[0])
    compressed.append(input2[1])
    difference.append(uncompressed[i]-compressed[i])
    sumCompressed += compressed[i]
if(sumCompressed>maximum):
    print(-1)
else:
    answer = 0
    difference.sort()
    for i in range(0, numSongs):
        if(sumCompressed+difference[i]<=maximum):
            sumCompressed+=difference[i]
            answer+=1
        else:
            break
    print(numSongs-answer)