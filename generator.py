def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(16):
    print(v)

t = [x for x in powers_of_2(20)]
print(t)