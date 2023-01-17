""" Write a Python program to get the n (non-negative integer) copies 
 of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2."""

nValue = input("Enter string: ")
n = int(input("Ente number: "))
if len(nValue) < 2 & n >= 0:
    for i in range(0, n):
        print(nValue)
elif len(nValue) >= 2 & n >= 0:
    for i in range(0, n):
        print(nValue[0:2:])
else:
    print("Please enter non negative number: ")
