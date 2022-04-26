import random as r 

def trial():
    total = 0
    for x in range(17):
        total += r.randint(0,4)
    return total / 52

def sim(t):
    total = 0
    for x in range(t):
        total += trial()
    return total / t

print(sim(40000))