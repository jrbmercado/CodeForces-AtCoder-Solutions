from collections import Counter

userName = input()
res = Counter(userName)
if(len(res)%2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")