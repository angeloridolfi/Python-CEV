print('Multiplos de três, até 500')

s = 0
v = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        v += 1
        print(i)
print(f'total de valores = {v}')
print('Soma =', s)
