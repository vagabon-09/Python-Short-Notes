# 8.	Write a Python program to calculate number of days between two dates. Sample dates : (2014, 7, 2), (2014, 7, 11).
year = int(input("Enter year: "))
month = int(input("Enter months: "))
day = int(input("Enter day: "))

year2 =int(input("Enter second year: "))
month2 =int(input("Enter second month: "))
day2 =int(input("Enter second day: "))

year_day = ((year2-year)*12)*30 # we are assuming all month complete with 30 days
month_day = ((month2-month))*30;
day_day= (day2-day);

print(f'there fore all days are: {year_day+month_day+day_day}')
