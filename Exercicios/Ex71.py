print('{:^20}'.format('Banco Angelito'))
print('=-' * 35)

n = int(input('Digite o valor a ser sacado: '))
total = n
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Foram necessárias {totalced} de {ced}!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Fim do programa!')
