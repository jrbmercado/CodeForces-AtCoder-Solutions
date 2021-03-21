year = str(int(input())+1)
setYear = {""}
while True:
    for i in range(0,4):
        setYear.add(str(year[i]))
    if(len(setYear)-1== 4):
        print(year)
        break
    else:
        year = str(int(year)+1)
        setYear={""}