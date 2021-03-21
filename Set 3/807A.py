# Grab first line
numPeople = int(input())

before = []
after = []
rated = False
unrated = False
maybe = False
for i in range(0, numPeople):
    input2 = list(map(int, input().split(" ")))
    before.append(input2[0])
    after.append(input2[1])

# Test for change in rank = rated
for i in range(0, numPeople):
    if(before[i] != after[i]):
        rated = True
        break

# Test for unrated, should be in order
for i in range(0, numPeople-1):
    if(before[i+1] > before[i]):
        unrated = True
        break

if(rated):
    print("rated")
elif(unrated):
    print("unrated")
else:
    print("maybe")