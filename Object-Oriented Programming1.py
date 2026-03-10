# Create a class for Robot
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)

# Create objects
tom = Robot("Tom")
jerry = Robot("Jerry")

# Make the robots introduce themselves
tom.introduce()
jerry.introduce()

