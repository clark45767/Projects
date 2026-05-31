# Program to check if a number is a power of 8 using bitwise operators

def is_power_of_8(n):
    """Check if n is a power of 8 using bitwise operations"""
    if n <= 0:
        return False
    
    # A number is power of 8 if it is power of 2 AND the exponent is multiple of 3
    # First check if it's power of 2: n & (n-1) == 0
    if (n & (n - 1)) != 0:
        return False
    
    # Now check if it's power of 8 by repeatedly dividing by 8
    while n > 1:
        if (n & 7) != 0:   # Last 3 bits must be 000
            return False
        n = n >> 3         # n = n // 8
    
    return True


# Main Program
print("=== Power of 8 Checker ===")

while True:
    try:
        num = int(input("\nEnter your number: "))
        
        if is_power_of_8(num):
            print(f"Yes  {num} is the power of 8")
        else:
            print(f"No  {num} is not the power of 8")
            
    except ValueError:
        print("Please enter a valid positive integer.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break