# Create a class
class Expression:
    # Constructor to initialize attributes
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    # Method to calculate addition
    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("The sum is:", result)

# Create objects
obj1 = Expression(5, 10, 15)
obj2 = Expression(2, 4, 6)

# Call the method
obj1.add_numbers()
obj2.add_numbers()