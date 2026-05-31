# Program to reverse all bits of a number using bitwise operations

def reverse_bits(n):
    """Reverse the bits of a number"""
    if n == 0:
        return 0
    
    # Get binary representation without '0b'
    binary = bin(n)[2:]
    # Reverse the binary string
    reversed_binary = binary[::-1]
    # Convert back to integer
    return int(reversed_binary, 2)

# Main program
print("Bit Reversal Program")
print("=" * 30)

while True:
    try:
        num = int(input("\nEnter your original number: "))
        if num < 0:
            print("Please enter a non-negative number.")
            continue
            
        reversed_num = reverse_bits(num)
        
        # Show binary representations
        original_bin = bin(num)[2:]
        reversed_bin = bin(reversed_num)[2:].zfill(len(original_bin))
        
        print(f"{num} ({original_bin})")
        print(f"Reversed Number : {reversed_num} ({reversed_bin})")
        
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break