n = int(input())
count = 0
for i in range(1, n):
    c = n//i
    if(n%i==0):
        c=c-1
    count+=c
print(count)