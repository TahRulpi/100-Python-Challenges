from array import *

arr = array('i', [1, 2, 3, 4, 5])
n = len(arr)
k = int(input("Enter value: "))

# Create a temporary array to store the shifted elements
temp_arr = array('i', [0] * n)

for i in range(n):
    new_index = (i + k) % n  # Calculate the new index after shifting
    temp_arr[new_index] = arr[i]

# Copy the shifted elements back to the original array
for i in range(n):
    arr[i] = temp_arr[i]

print(arr)