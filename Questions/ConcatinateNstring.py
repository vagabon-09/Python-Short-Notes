# 32.	 Write a Python program to concatenate N strings.

n = int(input("How many degits you want to concatinate ?"))
str = ""
for i in range(0, n):
    strmain = input("Enter a string :")
    str += strmain
print(str)
