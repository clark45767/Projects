import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 and 9
arr = np.arange(10)
print("Original Array:")
print(arr)

# 2. Replace all odd numbers with -1 without modifying the original array
arr_modified = np.where(arr % 2 == 1, -1, arr)
print("\nArray with odd numbers replaced by -1:")
print(arr_modified)

# 3. Convert the original 1-D array into a 2-D array with 2 rows
arr_2d = arr.reshape(2, 5)
print("\n2-D Array (2 rows):")
print(arr_2d)

# 4. Iterate through the original array and find the sum of all even numbers
sum_even = 0
for num in arr:
    if num % 2 == 0:
        sum_even += num

print("\nSum of all even numbers:", sum_even)