import random

def random_not_in(n, l):
    arr = range(n)
    z = list(set(arr) - set(l))
    print("list: ", z)
    return random.choice(z)

print(random_not_in(10,[3,5,7]))

