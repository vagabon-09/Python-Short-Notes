# 28.	 Write a Python program to convert all units of time into seconds.
dayS = int(input("Enter the day number: "))*(3600*24)
hour = int(input("Enter the number of hour: "))*3600
min = int(input("Enter the number of min: "))*60
time = int(dayS+hour+min)
print(time)
