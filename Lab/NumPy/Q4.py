# Write a NumPy program to test if any of the elements of a given array are non-zero.

import numpy as num;
arr = num.array([0,0,0,0,0,0,0,0,0]);
position = "";
for i in range(len(arr)):
    if arr[i] != 0:
        position=position+" "+str(i)+",";

print(f'only position {position} element are non base elements');

# also we can use any() function to check is there have any nonezero elemnts in the list or array
check = any(arr)
print(check)

