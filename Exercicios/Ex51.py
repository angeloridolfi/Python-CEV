print('P.A')

p = int(input('Digite o primeiro termo da P.A: '))
raz = int(input('Digite a razão da P.A: '))
dec = p + (10 - 1) * raz
for c in range(p, dec + 1, raz):
    print(c, end=' -> ')
print('Fim!')
