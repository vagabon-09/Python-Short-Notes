# 29.	 Write a Python program to convert seconds to day, hour, minutes, and seconds.
sec = int(input("Enter sec: "))
if sec >= 60:
    min = sec//60
    print(min)
elif sec >= 3600:
    hour = sec//3600
    print(hour)
elif sec >= 3600*24:
    day = sec//(3600*24)
    print(day)
else:
    print(sec)
