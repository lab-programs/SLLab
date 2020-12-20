# Part A: Program 05
# Write programs on:

# 1. Program to illustrate List Comprehension

l1 = [1, 2, 3, 4, 4, 5, 6, 7, 7]

l2 = [i for i in l1 if i%2 == 0]

print("Even numbers in l1 found using list comrehension are:", l2)

# 2. Program to illustrate Dictionary comprehension

d = {}

for i in l1:
    if i%2 == 0:
        d[i] = i**2
        
print("Output dictionary:", d)

# 3. Program to illustrate Lambda function

a = lambda a, b : a**b

print("5**3 done using lambda", a(5, 3))


# 4. Program to illustrate reduce function

from functools import reduce

sum = reduce((lambda x, y : x+y), l1)
print(sum)
