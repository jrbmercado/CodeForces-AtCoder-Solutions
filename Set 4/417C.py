input1 = list(map(int, input().split(" ")))
n = input1[0]
k = input1[1]
m = n-1
totalGamesPlayed = m+(m*(m-1))//2
if(k*n>totalGamesPlayed):
    print("-1")
else:
    print(n*k)
    for i in range(1,n+1):
        j=i+1
        while(j<=i+k):
            if(j>n):
                print(str(i) + " " + str(j%n))
            else:
                print(str(i) +  " " + str(j))
            j+=1