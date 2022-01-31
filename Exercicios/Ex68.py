from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
contador = 0
while True:
    computador = randint(1, 10)
    n = int(input('DIGITE UM NÚMERO: '))
    pi = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print('=' * 45)
    s = computador + n
    if pi == 'P':
        if s % 2 == 0:
            print('DEU PAR!')
            print('=' * 45)
            print(f'Você escolheu {n} e o computador escolheu {computador}. TOTAL = {s}')
            print('Você venceu. Parabéns!')
            contador += 1
        else:
            print('DEU ÍMPAR!')
            print('=' * 45)
            print(f'Você escolheu {n} e o computador escolheu {computador}.TOTAL = {s}')
            print('O computador venceu!')
            break
    if pi == 'I':
        if s % 2 != 0:
            print('DEU ÍMPAR!')
            print('=' * 45)
            print(f'Você escolheu {n} e o computador escolheu {computador}.TOTAL = {s}')
            print('Você venceu. Parabéns!!')
            contador += 1
        else:
            print('DEU PAR!')
            print('=' * 45)
            print(f'Você escolheu {n} e o computador escolheu {computador}.TOTAL = {s}')
            print('Computador venceu!')
            break
    print('=-' * 22)
print(f'Fim de jogo! Você venceu {contador} vezes no total.')
