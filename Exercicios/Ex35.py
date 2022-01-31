# Coletando os valores da reta.

r = float(input('Qual o valor da primeira reta: '))
r2 = float(input('Qual o valor da segunda reta: '))
r3 = float(input('Qual o valor da terceira reta: '))

# Determinando se as retas conseguem formar um um trângulo.

if r < r3 + r2 and r2 < r3 + r and r3 < r2 + r:
    print('Essas retas conseguem formar triângulo.')

else:
    print('Essas retas não conseguem formar um triângulo.')
