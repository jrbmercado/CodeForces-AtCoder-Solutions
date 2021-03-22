s = input()
consecutiveDays = 0
maxDays = 0
for i in range(0,3):
    if(s[i]=="R"):
        consecutiveDays+=1
    if(s[i]=="S"):
        consecutiveDays=0
    if(consecutiveDays>=maxDays):
        maxDays=consecutiveDays
print(maxDays)