testCases = int(input())
answers = []
for i in range(testCases):
    input1 = list(map(int, input().split(" ")))
    x = input1[0]
    y = input1[1]
    if(x%2==0):
        answer = y*(x//2)
    elif (y%2==0):
        answer = x*(y//2)
    else:
        answer = y*(x//2)+(y//2)+1
    answers.append(answer)
for i in answers:
    print(i)