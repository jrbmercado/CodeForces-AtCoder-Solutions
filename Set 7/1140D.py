vert = int(input())
minWeight = 0
for i in range(2, vert):
    minWeight += i*(i+1)
print(minWeight)