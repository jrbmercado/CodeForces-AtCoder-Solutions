testCases = int(input())
answers = []
for i in range(testCases):
    input1 = list(map(int, input().split(" ")))
    a = input1[0]
    b = input1[1]
    c = input1[2]
    d = input1[3]
    answer = str(b)+ " " + str(c) + " " + str(c)
    answers.append(answer)
for i in answers:
    print(i)