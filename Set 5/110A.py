from collections import Counter

number = input()
cnts = Counter(number)
numberOfLucky = cnts["7"]+cnts["4"]
if(numberOfLucky == 7 or numberOfLucky ==4):
    print("YES")
else:
    print("NO")