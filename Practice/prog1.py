# Matrix in python
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]

sum = []

for i in range(0,len(matrix)):
    num = 0
    for j in range(0, len(matrix[i])):
        num = num+matrix[i][j]
    sum.append(num)



print(sum)


   
   

# for i in range(len(matrix)):
#     print(sum[i])

