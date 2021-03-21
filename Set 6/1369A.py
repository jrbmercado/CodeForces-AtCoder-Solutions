testCases = int(input())
answers = []
for i in range(testCases):
    sides = int(input())
    if (sides%4 == 0):
        answer = "YES"
    else:
        answer = "NO"
    answers.append(answer)
for i in answers:
    print(i)