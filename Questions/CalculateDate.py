# 8.	Write a Python program to calculate number of days between two dates. Sample dates : (2014, 7, 2), (2014, 7, 11).
import calendar
from datetime import date
d1=date(2014,7,2)
d = date(2014,7,11)
print((d-d1).days)