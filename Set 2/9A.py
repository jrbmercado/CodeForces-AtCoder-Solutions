from fractions import Fraction
input1 = list(map(int,input().split(" ")))
y = input1[0]
w = input1[1]
maxRoll = max(y,w)
if(maxRoll==1):
    print("1/1")
elif(maxRoll==2):
    print("5/6")
elif(maxRoll==3):
    print("2/3")
elif(maxRoll==4):
    print("1/2")
elif(maxRoll==5):
    print("1/3")
else:
    print("1/6")