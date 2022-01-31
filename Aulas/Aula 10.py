n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')

if m >=6:
    print('sua média foi boa, top!')
else:
    print('Estuda mais ai pow')
