# Program to check Armstrong number

# Take input from user
num = int(input("Enter a positive integer: "))

# Store original number
original_num = num

# Count number of digits (order n)
num_str = str(num)
n = len(num_str)

# Calculate sum of digits raised to power n
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** n

# Check if Armstrong
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is NOT an Armstrong number.")
