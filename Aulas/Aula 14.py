# Estrutura de repetição
# While

'''for c in range(1, 10):
    print(c)
print('fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} impares.')
print('acabou')


