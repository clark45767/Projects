# Program to find all 2-digit prime numbers

def is_prime(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Find and print all 2-digit prime numbers
print("2-Digit Prime Numbers:")
primes = []
for number in range(10, 100):  # From 10 to 99
    if is_prime(number):
        primes.append(number)

# Print the results
print(primes)

# Optional: Print with nice formatting
print("\nThere are", len(primes), "two-digit prime numbers:")
for p in primes:
    print(p, end=" ")