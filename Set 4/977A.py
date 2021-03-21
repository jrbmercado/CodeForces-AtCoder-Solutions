input1 = list(map(int, input().split(" ")))
number = input1[0]
numSubtractions = input1[1]
for i in range(0, numSubtractions):
    if(str(number)[-1]=="0"):
        number = int(str(number)[:-1])
    else:
        number-=1
print(number)