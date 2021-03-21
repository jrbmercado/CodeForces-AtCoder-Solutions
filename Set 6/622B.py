input1 = list(map(int, input().split(":")))
input2 = int(input())
hours = input1[0]*60
minutes = input1[1]
totalMinutes = hours+minutes+input2
newHours = (totalMinutes//60)%24
newMinutes = totalMinutes%60
if(newHours<10):
    newHours = "0"+str(newHours)
if(newMinutes<10):
    newMinutes = "0"+str(newMinutes)
print(str(newHours)+":"+str(newMinutes))