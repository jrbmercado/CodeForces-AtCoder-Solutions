data = input()
sumOfData = 0
for i in range(0, len(data)):
  sumOfData+=int(data[i])
if(sumOfData%9 == 0):
  print("Yes")
else:
  print("No")