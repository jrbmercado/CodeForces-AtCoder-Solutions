input1 = list(map(int, input().split(" ")))
n = input1[0]
m = input1[1]

# Pattern1 has # at end for every even interval
pattern1 = ""
for i in range(0, m-1):
    pattern1 += "."
pattern1+="#"

# Pattern2 has # at beginning for every even interval
pattern2 = "#"
for i in range(0, m-1):
    pattern2 += "."

# Row has full line of # for every odd interval
row = ""
for i in range(0,m):
    row += "#"

counter = 1
pattern1Flag = True
pattern2Flag = False
while(n+1>1):
    #print("n= " + str(n)) 
    # If odd
    if (counter%2==0):
        if(pattern1Flag):
            print(pattern1)
            pattern1Flag = False
            pattern2Flag = True
        elif(pattern2Flag):
            print(pattern2)
            pattern1Flag = True
            pattern2Flag = False
    else:
        print(row)
    counter+=1
    n-=1