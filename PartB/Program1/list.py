def removeDuplicates(l):
    return list(dict.fromkeys(l))

# Read input from the user
listUnformatted = str(input())

l = listUnformatted.split(' ')
l = removeDuplicates(l)
print(l)

# List of even numbers in [0, 9]
evenNumbers = [i for i in range(10) if i%2 == 0]
print(evenNumbers)
# Reverse
evenNumbers.reverse()
print(evenNumbers)
