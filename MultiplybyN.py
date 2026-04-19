 # Function using 1 iteration (direct multiplication)
def one_iteration(a, b):
    return a * b

# Function using N iterations (repeated addition)
def n_iteration(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

# Input
a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

# Output
print("\n1 iteration: ", one_iteration(a, b))
print("N iteration: ", n_iteration(a, b))