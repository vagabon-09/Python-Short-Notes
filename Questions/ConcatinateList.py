# Write a Python program to concatenate all elements in a list into a string and return it.
list = ["a","b","c","d"]
conList= ""
for i in range(0,len(list)):
    conList += list[i]

print(conList)
