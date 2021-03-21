numTests = int(input())
arrayOfTests = []
for i in range(0, numTests):
    test = list(map(int, input().split(" ")))
    arrayOfTests.append(test)
for i in range(0, numTests):
    test = arrayOfTests[i]
    a = max(test[0], test[1])
    b = min(test[0], test[1])
    if(a>=2*b):
        sideSquare = a*a
    else:
        sideSquare = (2*b)*(2*b)
    print(sideSquare)