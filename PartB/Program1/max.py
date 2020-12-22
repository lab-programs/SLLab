import random

def maximum(l):
    if len(l) == 1:
        return l[0]
    
    m = maximum(l[1:])
    return m if m > l[0] else l[0]
    
l = [random.randint(0, 10) for _ in range(10)]
print(l)
print(maximum(l))