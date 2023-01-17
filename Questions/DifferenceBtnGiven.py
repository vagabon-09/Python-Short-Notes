# 9.Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
value = int(input("Enter number: "))
if value > 17:
    print((17-value)*(17-value))
else:
    print((17-value))