s = list(map(int, input().split("+")))
s.sort()
result=""
for i in range(0,len(s)):
    result += str(s[i])
    if(i!=len(s)-1):
        result+="+"
print(result)