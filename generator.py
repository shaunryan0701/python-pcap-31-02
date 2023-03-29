def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(16):
    print(v)

t = [x for x in powers_of_2(20)]
print(t)


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

# List comprehension becoming a generator
for x in (el * 2 for el in range(5)):
    print(x)