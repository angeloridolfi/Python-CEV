print('PRIMO!')
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
        tot += 1
        print('\033[32m',end=' ')
    else:
        print('\033[31m',end=' ')
    print(c,end=' \033[m')
if tot == 2:
    print(f'\nO número {num} é primo!')
else:
    print(f'\nO número {num} foi dividido {tot} vezes, então não é primo!')
