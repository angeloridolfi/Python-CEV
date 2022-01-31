n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
esc = 0

while esc != 5:
    esc = int(input('''
    O que vocẽ deseja fazer com os valores?
    ========================================
    [ 1 ] somar.
    [ 2 ] multiplicar.
    [ 3 ] maior.
    [ 4 ] novos números
    [ 5 ] sair do programa!
    ========================================
    Digite a sua opção aqui: '''))
    if esc == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}!')
    elif esc == 2:
        print(f'O resultado da multiplicação entre {n1} e {n2} é igual a {n1 * n2}!')
    elif esc == 3:
        if n1 > n2:
            print(f'O maior é {n1}!')
        elif n2 > n1:
            print(f'O maior é {n2}!')
        else:
            print('Valores iguais!')
    elif esc == 4:
        n1 = float(input('Digite um novo valor: '))
        n2 = float(input('Digite mais um novo valor: '))
    elif esc == 5:
        print('saindo...')
    else:
        print('Valor inválido! Tente novamente!')

