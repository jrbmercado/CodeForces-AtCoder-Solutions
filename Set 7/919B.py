kInt = int(input())
perfect = 18
sum1 = 0
count = 0
while(sum1!=kInt):
    perfect+=1
    count = 0
    i = perfect
    while(i!=0):
        count+=i%10
        i= i//10
    if(count==10):
        sum1+=1
print(perfect)