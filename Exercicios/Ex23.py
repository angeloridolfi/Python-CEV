num = int(input('Digite um número de 0 a 9999:\n'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 100
m = num // 1000 % 1000

print(f'Analisando o número {num}')
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'Centena:{c}')
print(f'Milhar:{m}')
