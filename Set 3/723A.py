input1 = list(map(int,input().split(" ")))
input1.sort()

person1 = input1[0]
person2 = input1[1]
person3 = input1[2]

# Calculate person1 distance to person2
differenceP1P2 = abs(person1-person2)

# Calculate person3 distance to person2
differenceP3P2 = abs(person3-person2)

total = differenceP1P2 + differenceP3P2
print(total)