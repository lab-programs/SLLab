# Part A: Program 01
# Python Introduction - Simple Programs in Python based on:

# Selection Constructs

print("**** Select Constructs ****")

a = input("Enter value of a: ")
print("The value of a is:", a)

b = input("Enter value of b: ")
print("The value of b is:", b)

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print(a, "and", b, "are equal")
    

# Looping Constructs

print("**** Looping Constructs ****")

for n in range(2, 10):
    for x in range(2, 1 + n//2):
        if n%x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")
