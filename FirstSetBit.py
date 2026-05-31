# Program to find the position of the rightmost set bit

def rightmost_set_bit_position(n):
    """Find the position of the rightmost set bit (1-based indexing)"""
    if n == 0:
        return 0  # No set bits
    
    position = 1
    # Keep shifting right until we find the first set bit
    while (n & 1) == 0:
        n = n >> 1
        position += 1
    
    return position

# Main program
print("Rightmost Set Bit Finder")
print("=" * 30)

while True:
    try:
        num = int(input("\nEnter number: "))
        if num < 0:
            print("Please enter a positive number.")
            continue
            
        pos = rightmost_set_bit_position(num)
        
        # Show binary representation
        binary = bin(num)[2:]  
        print(f"{num} ({binary})")
        
        if pos == 0:
            print("No set bits (number is 0)")
        else:
            print(f"Position of the first set bit: {pos}")
            
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break