# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
value = input("Enter your string: ")
vRange = int(input("Enter range: "))

if vRange >0:
    for i in range(0,vRange):
        print(value+ " ")
else:
    print("Please enter non negetiv value ")
