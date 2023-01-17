# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
sValue = input("Enter a word ")
if sValue[0:2:] == "is" : 
    print(sValue)
else:
    print("is "+sValue)

