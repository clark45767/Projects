# Recursive function to find Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask user how many terms they want
terms = int(input("Enter the number of terms: "))

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")