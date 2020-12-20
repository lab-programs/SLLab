# Part A: Program 04
# Programs based on:

# 1. Function

# a. Create a function to print "Hello, World!"

def printText():
    print("Hello, World!")
    return
    
printText()

# b. Create a function to print two integers taken as parameters

def printTwoValues(a, b):
    print("THe values of a and b are", a, "and", b)
    return
    
printTwoValues(10, 20)

# c. Create a function to illustrate default values for a
# parameter for the previous program

def printTwoValuesDefault(a, b=5):
    print("The values of a and b are", a, "and", b)
    return
    
printTwoValuesDefault(10)

# d. Create a function to illustrate keyword arguments using
# the previous program

def printTwoValuesKeyWord(a, b):
    print("The values of a and b are", a, "and", b)
    return
    
printTwoValuesKeyWord(b=20, a=10)

# 2. Recursive Function

# e. Write a recursive function to find factorial of a number

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
    
a = factorial(5)
print("Factorial(5) =", a)

# 3. Class

# f. Write a Class to encapsulate a Complex number

class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

x = Complex(3.5, 3.5)
print("x =", x.real, "+", str(x.imaginary) + "i")
