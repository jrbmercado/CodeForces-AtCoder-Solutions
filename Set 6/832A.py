numbers = list(map(int, input().split(" ")))
totalSticks = numbers[0]
step = numbers[1]
if(totalSticks//step%2 == 0):
    print("NO")
else:
    print("YES")