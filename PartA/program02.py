# Part A: Program 02
# Using Python - Simple Problems in Python based on:

# 1. List

print("\n**** List Operations ****")

a = [12, 24, 36, 48, 60]

print("Set of values of list:", a[2:4])
print("Retrieve using negative indexing:", a[-2])

print("Unmodified List:", a)
a[3] = "New article"
print("List after changing:", a)

del a[3]
print("List after deleting:", a)

a.insert(1, 0)
print("List after inserting at a position:", a)

a.reverse()
print("Reversed List:", a)

a.sort()
print("Sort:", a)


# 2. Tuple

print("\n**** Tuple Operations ****")

t1 = (15, 30, 45, 60, 75)
t2 = ('a', 'b', 'c')
t3 = t1+t2

print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Concatenated Tuple 1 & Tuple 2 = Tuple 3:", t3)

del t3
# print(t3) will raise an exception since we deleted t3

print("Maximum element in  t1:", max(t1))
print("Minimum element in  t1:", min(t1))
print("Number of elements in t1:", len(t1))


# 3. Dictionary

print("\n**** Dictionary Operations ****")

d = {
    1: 'amazon',
    2: 'flipkart',
    3: 'Alibaba',
    4: 'Croma'
}

print("Dictionary is:", d)
print("Retrieving first value:", d[1])

del d[4]
print("Dictionary after deleting d[4]:", d)

print("List of key-value pairs:", d.items())

print("List of keys:", d.keys())
print("List of values:", d.values())

e = d.copy()
print("Copy in Dictionary:", e)

d.clear()
print("Dictionary after clear:", d)
