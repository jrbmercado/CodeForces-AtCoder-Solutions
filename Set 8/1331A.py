numTests = int(input())
answers = []
while(numTests>0):
    input1 = list(map(int, input().split(" ")))
    a = input1[0]
    b = input1[1]
    answer = 0
    # Determine which one is bigger
    if(a==b):
        answer = 0
    elif (a<b):
        # If 1 is odd and 1 is even
        if((a+b)%2==1):
            answer = 1
        else: # Else they are both odd or both even
            answer = 2
    else:
        # If 1 is even and 1 is odd
        if((a-b)%2==1):
            answer = 2
        else: # Else they are both odd or both even
            answer = 1
    answers.append(answer)
    numTests -= 1
for i in answers:
    print(i)