import random
def Random7():
    a = random.randint(1,5)
    b = random.randint(1,5) - 3
    if (b > 0):
        a = a + b
    return a
print(Random7())