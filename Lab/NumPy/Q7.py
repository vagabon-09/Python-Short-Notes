# Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np
arr = np.array([1,2,3,4,np.NAN,np.inf,np.NINF])

for i in range(len(arr)):
    if np.isnan(arr[i]):
        print(f'yes position {i+1} is a NAN value')
