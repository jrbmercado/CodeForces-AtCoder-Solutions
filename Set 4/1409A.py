numTests = int(input())
arrayOfTests = []
for i in range(0, numTests):
    test = list(map(int, input().split(" ")))
    arrayOfTests.append(test)
for i in range(0, numTests):
    count = 0
    test = arrayOfTests[i]
    a = test[0]
    b = test[1]
    r = abs(a-b)
    count += r//10
    r-=10*count
    if(r>0):
        count+=1
    print(count)