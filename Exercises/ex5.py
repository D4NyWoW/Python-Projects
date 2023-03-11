# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class String():
    def __init__(self):
        self.str = ""
    
    def input_string(self):
        self.str = input()

    def upper_string(self):
        print(self.str.upper())

str1 = String()
str1.input_string()
str1.upper_string()