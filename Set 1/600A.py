data = input()
data = str(data.replace(",", ";"))
data = data.split(";")
a = "NONE"
b = "NONE"
for i in data:
    if(i=="0" and a!="NONE"):
        a+="0" + ","
    elif(i=="0" and a=="NONE"):
        a="0" + ","
    elif(i.isdigit() and int(i)>0 and not i.startswith("0") and a!="NONE"):
        a+=i+",";
    elif(i.isdigit() and int(i)>0 and not i.startswith("0") and a=="NONE"):
        a=i+",";
    elif(b=="NONE"):
        b=i+",";
    else:
        b+=i+",";

if(a[:-1] == "NON"):
  print("-")
else:
  print('"'+ a[:-1]+'"')
if(b[:-1] == "NON"):
  print("-")
else:
  print('"'+b[:-1]+'"')