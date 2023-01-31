# 27.	 Write a Python program to convert the distance (in feet) to inches, yards, and miles.
feet = float(input("Enter feet value: "))
inches = float(feet*12)
print(inches)
yard = float(feet*0.3333)
print(yard)
mile = float(feet*(1/5280))
print(mile)
