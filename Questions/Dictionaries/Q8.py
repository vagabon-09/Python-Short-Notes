dic ={1:'Mango',3:'Oranges',2:'Banana',4:'Goava'}

keyList = list(dic.keys())
keyList.sort()
print(keyList)
newDic={i:dic[i] for i in keyList}

print(newDic)
