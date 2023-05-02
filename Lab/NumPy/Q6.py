import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,np.inf,np.NINF])
for i in arr:
    if i>0:
     print(np.isfinite(i))
    else:
        print(f'negative {i} is {np.isfinite(i)}')