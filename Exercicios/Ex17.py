from math import hypot

n = float(input('Digite o valor do cateto oposto:'))
n2 = float(input('Digite o valor do cateto adjacente:'))

print(f'O triangulo com os catetos que medem: {n} e {n2} tem a hipotenusa igual á: {hypot(n,n2):.2f}')
