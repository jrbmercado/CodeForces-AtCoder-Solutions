numTests = int(input())
answers = []
while numTests > 0:
    testLen = int(input())
    answer = ""
    for i in range(0, testLen):
        if i % 2 == 0:
            answer += "1 "
        else:
            answer += "1 "
    answers.append(answer)
    numTests -= 1
for i in answers:
    print(i)