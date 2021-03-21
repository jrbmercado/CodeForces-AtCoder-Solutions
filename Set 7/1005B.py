word1 = input()
word2 = input()
absDifference = abs(len(word1)-len(word2))
if(len(word1)>len(word2)):
    word1 = word1[absDifference:]
else:
    word2 = word2[absDifference:]
moves = absDifference
timeBroken = len(word1)-1
for i in range(len(word1)-1,-1,-1):
    if(word1[i]==word2[i]):
        continue
    else:
        timeBroken = i
        moves+=2*(timeBroken+1)
        break
print(moves)