n = int(input())
for i in range(0,n):
    if(i%2==1):
        j = 0
        while j<n:
            print("B", end="")
            j += 1
            if(j<n):
                print("W", end="")
            j += 1 
        print("")
    else:
        j = 0
        while j<n:
            print("W", end="")
            j += 1
            if(j<n):
                print("B", end="")
            j += 1
        print("")