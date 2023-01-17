# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
val1 = int(input("Enter value 1: "));
val2 = int(input("Enter value 2: "));
val3 = int(input("Enter value 3: "));

if val1 == val2 & val2 == val3:
    print(3*(val1+val2+val3))
else:
    print(val1+val2+val3)