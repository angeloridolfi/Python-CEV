c = int(input('Digite um número para ver seu fatorial: '))
multiplicador = 1
print(f'{c}!',end='=')
while c > 0:
    print(c,end='')
    print('x' if c > 1 else '=',end='')
    multiplicador *= c 
    c -= 1
print(f'{multiplicador}')
print('\nObrigado!')
