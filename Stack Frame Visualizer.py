# ================================
# STACK FRAME VISUALIZER
# ================================
# Topics:
# Linear Recursion | Tail Recursion | Head Recursion
# Increasing-Decreasing Recursion | Tree Recursion

print("================================")
print("STACK FRAME VISUALIZER")
print("================================")


# --------------------------------
# PART 1 - LINEAR RECURSION
# --------------------------------

def linear_recursion(n):
    if n == 0:
        return

    print("Linear call at level:", n)
    linear_recursion(n - 1)


print("\nPART 1: Linear Recursion")
linear_recursion(5)


# --------------------------------
# PART 2 - TAIL RECURSION
# --------------------------------

def tail_recursion(n):
    if n == 0:
        return

    print("Tail work before call:", n)
    tail_recursion(n - 1)


print("\nPART 2: Tail Recursion")
tail_recursion(5)


# --------------------------------
# PART 3 - HEAD RECURSION
# --------------------------------

def head_recursion(n):
    if n == 0:
        return

    head_recursion(n - 1)
    print("Head work after call:", n)


print("\nPART 3: Head Recursion")
head_recursion(5)


# --------------------------------
# PART 4 - INCREASING-DECREASING RECURSION
# --------------------------------

def increasing_decreasing(n):
    if n == 0:
        return

    print("Going down:", n)
    increasing_decreasing(n - 1)
    print("Coming back:", n)


print("\nPART 4: Increasing-Decreasing Recursion")
increasing_decreasing(5)


# --------------------------------
# PART 5 - TREE RECURSION
# --------------------------------

def tree_recursion(n):
    if n == 0:
        return

    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)


print("\nPART 5: Tree Recursion")
tree_recursion(3)


# --------------------------------
# FINAL SUMMARY
# --------------------------------

print("\n================================")
print("RECURSION PATTERN SUMMARY")
print("================================")
print("Linear Recursion: One recursive call at each level.")
print("Tail Recursion: Work happens before the recursive call.")
print("Head Recursion: Work happens after the recursive call.")
print("Increasing-Decreasing: Work happens before and after the call.")
print("Tree Recursion: More than one recursive call at each level.")
print("================================")