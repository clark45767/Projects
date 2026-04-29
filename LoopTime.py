def myfunction(n):
    
    count1 = 0
    for i in range(0, n + 1):
        count1 += 1

    
    count2 = 0
    j = 1
    while j <= n + 1:
        count2 += 1
        j = j * 2

    
    count3 = 0
    for i in range(0, 100):
        count3 += 1

    # Print results
    print("First Loop runs:", count1, "times → O(n)")
    print("Second Loop runs:", count2, "times → O(log n)")
    print("Third Loop runs:", count3, "times → O(1)")

    print("\nTotal Time Complexity: O(n)")


# Test the function
myfunction(10)