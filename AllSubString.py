# Program to find and print all substrings of a given string

def find_all_substrings(s):
    """Generate and print all possible substrings"""
    print(f"\nAll substrings of '{s}':")
    substrings = []
    n = len(s)
    
    # Generate all substrings using two nested loops
    for i in range(n):           # Starting index
        for j in range(i + 1, n + 1):  # Ending index
            substring = s[i:j]
            substrings.append(substring)
            print(substring)
    
    print(f"\nTotal substrings: {len(substrings)}")
    return substrings


# Main Program
print("All Substrings Generator")
print("=" * 30)

while True:
    try:
        user_input = input("\nEnter string : ").strip()
        
        if not user_input:
            print("Please enter a non-empty string.")
            continue
            
        find_all_substrings(user_input)
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break