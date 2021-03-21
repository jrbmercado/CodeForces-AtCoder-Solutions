numTest = int(input())
arrCandies = []
for i in range(0, numTest):
    arrCandies.append(int(input()))
for i in arrCandies:
    if(i%2==0):
        print((i//2)-1)
    else:
        print(i//2)