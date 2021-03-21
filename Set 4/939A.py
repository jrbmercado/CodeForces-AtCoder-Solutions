numPlanes = int(input())
planes = list(map(int,input().split()))
currentPosition = 0
flag = True
for i in range(0,numPlanes):
    # Get value at index
    currIndexValue = planes[i]
    # Get value of the currentIndex's value
    nextIndexValue = planes[currIndexValue-1]
    # Get value of nextIndexValue
    lastIndexValue = planes[nextIndexValue-1]
    # If the value of the last index matches the index we're on then we have a triangle
    if(lastIndexValue-1 == i):
        print("YES")
        flag = False
        break
if(flag):
    print("NO")