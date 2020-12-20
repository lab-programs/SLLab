# Part A: Program 03
# Combining Python Basics and its Data Structures

# 1. Selection

print("\n**** Selection ****")
num = int(input("Enter any number: "))

if num%2 == 0:
    print(f'The number {num} is a even number')
else:
    print(f'The number {num} is a odd number')

# 2. Looping with Lists

print("\n**** Looping with Lists ****")
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
                
    return False
                
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# 3. Looping with Tuples

print("\n**** Looping with Tuples ****")
t = (10, 20, 30, 40, 50)
for v in t:
    print(t.index(v), v)
    
    
# 4. Looping with Dictionary

print("\n**** Looping with Dictionary ****")

def sum_math(list_d):
    for item in list_d:
        n1 = item.pop('V')
        n2 = item.pop('VI')
        item['V' + 'VI'] = (n1+n2)/2
    return list_d

st_det = [
    {'id':1, 'subj':'math', 'V':70, 'VI':82},
    {'id':2, 'subj':'math', 'V':25, 'VI':52},
    {'id':3, 'subj':'math', 'V':63, 'VI':87}
]

print(sum_math(st_det))
