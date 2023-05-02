dic = {1: "Rajesh", 2: "Akash", 3: "Rajesh", 4: "Ritik"}
dic2={}
for i in dic:
   if dic[i] not in dic2.values():
      dic2[i] = dic[i]
print(dic2)