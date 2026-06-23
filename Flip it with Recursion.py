# ================================
# FLIP IT WITH RECURSION
# ================================

# =============================================
# PART 1: Extracting Digits with % and //
# =============================================
print("PART 1: Extracting Digits with % and //")
number = 4827
temp = number
print(f"Original Number: {number}")

while temp > 0:
    last_digit = temp % 10
    remaining_number = temp // 10
    print(f"Last Digit: {last_digit} | Remaining Number: {remaining_number}")
    temp = remaining_number

print("-" * 40)

# =============================================
# PART 2: Count Digits Recursively (Helper)
# =============================================
def count_digits(num):
    if num < 10:          # Base case: single digit
        return 1
    return 1 + count_digits(num // 10)   # Recursive call

# =============================================
# PART 3: Reverse a Number with Recursion
# =============================================
def reverse_number(num):
    if num < 10:          # Base case: single digit
        return num
    last_digit = num % 10
    remaining = num // 10
    # Count digits in remaining number to shift last_digit to front
    digits_left = count_digits(remaining)
    return last_digit * (10 ** digits_left) + reverse_number(remaining)


# =============================================
# PART 4: Reverse a String with Recursion
# =============================================
def reverse_string(text):
    if len(text) <= 1:    # Base case: empty or single character
        return text
    # Recursive case: reverse the rest + put first character at the end
    return reverse_string(text[1:]) + text[0]


# =============================================
# PART 5: Check Powers of 4 with Recursion
# =============================================
def is_power_of_4(num):
    if num <= 0:          # Stopping condition 1: Invalid input
        return False
    if num == 1:          # Stopping condition 2: Success case
        return True
    if num % 4 != 0:      # Not divisible by 4
        return False
    return is_power_of_4(num // 4)   # Recursive call


# =============================================
# MAIN PROGRAM - TESTING
# =============================================
print("PART 2: Reversing a Number with Recursion")
num = 4827
print(f"Original Number : {num}")
print(f"Reversed Number : {reverse_number(num)}")
print("-" * 40)

print("PART 3: Reversing a String with Recursion")
word = "CODING"
print(f"Original String : {word}")
print(f"Reversed String : {reverse_string(word)}")
print("-" * 40)

print("PART 4: Checking Powers of 4 with Recursion")
test_numbers = [1, 4, 8, 16, 20, 64, 100, 256]
for value in test_numbers:
    print(f"{value} is power of 4: {is_power_of_4(value)}")
print("-" * 40)

# =============================================
# PART 6: Two Stopping Conditions Explanation
# =============================================
print("PART 5: Two Stopping Conditions in Recursion")
print("1. For numbers  (is_power_of_4):")
print("   - num <= 0   → stops invalid checks")
print("   - num == 1   → confirms it is a power of 4")
print("2. For strings (reverse_string):")
print("   - len(text) <= 1  → stops when string is empty or has one character")
print()
print("Stopping conditions are crucial to prevent infinite recursion!")

print("\n" + "="*50)
print("PROGRAM EXECUTED SUCCESSFULLY")
print("="*50)