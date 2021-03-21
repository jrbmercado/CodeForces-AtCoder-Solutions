t = input()
inPerson = 0
outPerson = 0

for i in range(0, len(t)):
    if(t[i]=="+"): 
        inPerson +=1
        if(outPerson):
            outPerson-=1
    elif(t[i]=="-"):
        outPerson +=1
        if(inPerson):
            inPerson-=1
print(inPerson+outPerson)