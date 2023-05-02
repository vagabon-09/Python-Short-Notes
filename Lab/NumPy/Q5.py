# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number)
import numpy as num
arr = num.array([1,2,3,5,num.inf,'a',4,5,6])
for i in range(len(arr)):
    if num.isreal(arr[i]) == True:
        if num.isfinite(arr[i]) == False :
            print(f'position { i } is not a finite value')
        else:
            print(f'position { i } is a finite value')
    else:
        print(f'value of position {i} is not a number')