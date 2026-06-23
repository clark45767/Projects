# ================================
# STAIR CLIMB AND BRACE BUILDER
# ================================
# Topics Covered:
# - Stair Climb Problem (Recursion)
# - Tracing Recursive Call Tree
# - Balanced Braces / Parentheses Generation

print("================================")
print("STAIR CLIMB AND BRACE BUILDER")
print("================================")

# =============================================
# PART 1 & 2: Stair Climb Problem
# =============================================
def stair_ways(n):
    """Returns the number of ways to climb n stairs (1 or 2 steps at a time)"""
    if n == 0:          # Successful stopping condition
        return 1
    if n < 0:           # Invalid path stopping condition
        return 0
    # Recursive case: ways taking 1 step + ways taking 2 steps
    return stair_ways(n - 1) + stair_ways(n - 2)


print("\nPART 2: Solving Stair Climb with Recursion")
stairs = 5
print(f"Number of stairs: {stairs}")
print(f"Total distinct ways: {stair_ways(stairs)}")
print("-" * 50)

# =============================================
# PART 3: Trace the Call Tree
# =============================================
def trace_stair_ways(n, space=""):
    """Prints the recursive call tree with indentation to visualize branching"""
    print(space + f"stair_ways({n})")
    
    if n == 0:
        print(space + "  → Reached base case (n==0), return 1")
        return 1
    if n < 0:
        print(space + "  → Invalid path (n<0), return 0")
        return 0
    
    # Recursive calls with increased indentation
    one_step = trace_stair_ways(n - 1, space + "    ")
    two_steps = trace_stair_ways(n - 2, space + "    ")
    
    total = one_step + two_steps
    print(space + f"  → Total ways for {n} stairs = {total}")
    return total


print("\nPART 3: Tracing the Call Tree (for 3 stairs)")
trace_stair_ways(3)
print("-" * 50)

# =============================================
# PART 4 & 5: Balanced Braces (Parentheses)
# =============================================
def generate_braces(current, open_count, close_count, total_pairs):
    """Generates all valid combinations of curly braces"""
    # Base case: when we have used all pairs
    if len(current) == total_pairs * 2:
        print(current)
        return
    
    # Add opening brace if we haven't used all
    if open_count < total_pairs:
        generate_braces(current + "{", open_count + 1, close_count, total_pairs)
    
    # Add closing brace only if we have more open than close
    if close_count < open_count:
        generate_braces(current + "}", open_count, close_count + 1, total_pairs)


print("\nPART 5: Balanced Braces (3 pairs)")
pairs = 3
print(f"Valid combinations for {pairs} pairs of braces:")
generate_braces("", 0, 0, pairs)
print("-" * 50)

# =============================================
# SUMMARY
# =============================================
print("\nSUMMARY")
print("• Stair climb uses two recursive calls: n-1 and n-2")
print("• Base cases: n == 0 (valid) and n < 0 (invalid)")
print("• Call tree shows how recursion branches and returns")
print("• Balanced braces: add '{' when possible, add '}' only when balanced")
print("• Recursion is powerful for exploring all possible paths!")
print("================================")