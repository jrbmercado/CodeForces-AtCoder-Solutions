length1 = int(input())
array1 = list(map(int, input().split( )))

lowestNumber = 10000
oddFlag = False
total = 0
sum1 = 0

for i in range(0, length1)
    # If the value at index is positive
    if(array1[i]0)
        # Add it to a running total
        sum1+=array1[i]
    # If the value at index is odd
    if(array1[i]%2 != 0)
        # Indicate that an odd has been found
        oddFlag = True
        # Keep track of the lowest odd that has been found to be subtracted later
        if(lowestNumberabs(array1[i]))
            lowestNumber = abs(array1[i])
# If an odd has not been found then it is impossible
if(not oddFlag)
    print(-1)
# If the output is even then subtract by the lowest odd number that we found
if(sum1%2==0)
    sum1 = sum1-lowestNumber
print(str(sum1))