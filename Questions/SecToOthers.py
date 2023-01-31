# 29.	 Write a Python program to convert seconds to day, hour, minutes, and seconds.
sec = int(input("Enter sec"))
day = sec//(3600*24)
min = sec//60
hour = sec//3600
print(day)
print(min)
print(hour)
