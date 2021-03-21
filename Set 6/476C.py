input1 = list(map(int, input().split(" ")))
a = input1[0]
b = input1[1]
quotient = b*(b-1)//2
remainder = a*(a+1)//2
answer = (quotient*((remainder*b)%(10**9+7)+a)%(10**9+7))
print(answer)