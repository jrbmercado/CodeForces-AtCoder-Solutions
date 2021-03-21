x = list(input())
y = list(input())
answerString = ""
impossible = False
for i in range(0, len(x)):
    if(x[i]==y[i]):
        if(x[i]<"z"):
            answerString+="z"
        else:
            answerString+=x[i]
    elif(x[i]>y[i]):
        answerString+=y[i]
    elif(x[i]<y[i]):
        impossible = True
        break

if(impossible):
    print("-1")
else:
    print(answerString)