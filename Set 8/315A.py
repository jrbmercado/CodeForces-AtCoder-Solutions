n = int(input())
list1 = []
list2 = []
openedBottles = []
for i in range(0, n+1):
    list1.append(0)
    list2.append(0)
    openedBottles.append(0)
for i in range(1, n+1):
    input1 = list(map(int, input().split(" ")))
    list1[i] = input1[0]
    list2[i] = input1[1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if(i!=j and list2[i] == list1[j]):
            openedBottles[j] = 1
answer = 0
for i in range(1, n+1):
    answer += openedBottles[i]
print(n-answer)