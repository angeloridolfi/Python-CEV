from ast import Num


cont = soma = num = 0

while num != 999:
    num = int(input('Digite um número inteiro[999 para sair!]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        print('Saindo...')
print(f'Você digitou {cont} números e a soma entre eles é de {soma}!')
