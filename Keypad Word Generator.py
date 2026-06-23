# ================================
# KEYPAD WORD GENERATOR + TOWER OF HANOI
# ================================
# Topics: Recursive Thinking, Tower of Hanoi, Phone Keypad Combinations, Recursion Tree

print("================================")
print("KEYPAD WORD GENERATOR")
print("================================")

# =============================================
# PART 2: Tower of Hanoi (Recursive)
# =============================================
def tower_of_hanoi(disks, source, helper, destination):
    """Solve Tower of Hanoi recursively"""
    if disks == 1:                              # Base Case
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Recursive Step 1: Move n-1 disks to helper
    tower_of_hanoi(disks - 1, source, destination, helper)
    
    # Move the largest disk to destination
    print(f"Move disk {disks} from {source} to {destination}")
    
    # Recursive Step 2: Move n-1 disks from helper to destination
    tower_of_hanoi(disks - 1, helper, source, destination)


print("\nPART 2: Tower of Hanoi (3 disks)")
print("Moves required:")
tower_of_hanoi(3, "A", "B", "C")
print("-" * 50)

# =============================================
# PART 3: Phone Keypad Mapping
# =============================================
keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

# =============================================
# PART 4: Generate Keypad Words Recursively
# =============================================
def generate_words(remaining_digits, current_word):
    """Generate all possible letter combinations for given digits"""
    # Base Case: No digits left → print the complete word
    if len(remaining_digits) == 0:
        print(current_word)
        return
    
    first_digit = remaining_digits[0]
    rest_digits = remaining_digits[1:]
    
    # Try every letter for the current digit
    for letter in keypad[first_digit]:
        generate_words(rest_digits, current_word + letter)


print("\nPART 4: Phone Keypad Word Generator")
number = "23"
print(f"Input digits : {number}")
print("Possible words:")
generate_words(number, "")
print("-" * 50)

# =============================================
# PART 5: Trace the Recursion Tree
# =============================================
def show_recursion_tree(remaining_digits, current_word, level=0):
    """Visualize the recursion tree with indentation"""
    indent = "   " * level
    
    print(indent + f"Current: '{current_word}' | Remaining: {remaining_digits}")
    
    if len(remaining_digits) == 0:
        print(indent + f"✅ Word completed: {current_word}")
        return
    
    first_digit = remaining_digits[0]
    rest_digits = remaining_digits[1:]
    
    for letter in keypad[first_digit]:
        show_recursion_tree(rest_digits, current_word + letter, level + 1)


print("\nPART 5: Recursion Tree Trace (for digits '23')")
show_recursion_tree("23", "")
print("-" * 50)

# =============================================
# SUMMARY
# =============================================
print("\nSUMMARY")
print("• Recursion breaks big problems into smaller identical problems")
print("• Tower of Hanoi: Move n-1 → largest disk → n-1 again")
print("• Keypad: For each digit, try all letters recursively")
print("• Base case stops the recursion")
print("• More digits = exponentially more combinations")
print("================================")