# Program to find the longest consecutive 1's in binary representation

def longest_consecutive_ones(n):
    """Find the length of longest consecutive 1's using bitwise operations"""
    if n <= 0:
        return 0
    
    max_length = 0
    current_length = 0
    
    while n > 0:
        if n & 1:                    # Check if current bit is 1
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0       # Reset counter when 0 is found
        n = n >> 1                   # Right shift to check next bit
    
    return max_length


# Main Program
print("Longest Consecutive 1's in Binary")
print("=" * 40)

while True:
    try:
        num = int(input("\nEnter your number: "))
        
        if num < 0:
            print("Please enter a non-negative number.")
            continue
            
        length = longest_consecutive_ones(num)
        binary = bin(num)[2:]   # Get binary string without '0b'
        
        print(f"{num} ({binary})")
        print(f"Longest consecutive 1's length : {length}")
        
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break