# 14.	 Write a Python program to count the number 4 in a given list
arr = [1, 2, 4, 6, 4]
count = 0
for i in range(0, len(arr)):
    if arr[i] == 4:
        count +=1
print(count)
