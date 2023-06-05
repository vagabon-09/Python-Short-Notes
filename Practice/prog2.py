# Add two matrix 
import numpy as np
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]]

num = 0;
matrix3=np.empty((3,3))

for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
        matrix3[i][j] =  matrix[i][j]+matrix2[i][j]

print(matrix3)
print(np.array((5,4)))
