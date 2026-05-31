# Program to find LCM of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max(num1, num2)

while True:
    if largest % num1 == 0 and largest % num2 == 0:
        lcm = largest
        break
    largest += 1

print("LCM is:", lcm)