testCases = int(input())
answers = []
for i in range(testCases):
    input1 = list(map(int, input().split(" ")))
    hours = 23-input1[0]
    minutes = 60-input1[1]
    answer = hours*60+minutes
    answers.append(answer)
    
for i in answers:
    print(i)