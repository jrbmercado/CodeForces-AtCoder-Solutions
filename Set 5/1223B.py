testCases = int(input())
answer = []
for i in range(0, testCases):
    s1 = set(input())
    s2 = set(input())
    intersection = s1.intersection(s2)
    if(len(intersection)==0):
        answer.append("NO")
    else:
        answer.append("YES")
        
for i in range(0, len(answer)):
    print(answer[i])