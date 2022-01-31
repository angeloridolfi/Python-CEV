# Coletando os números.

n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Derterminando o maior número.

if n > n2 and n > n3:
    print(f'O número {n} é o maior!')

elif n2 > n and n2 > n3:
    print(f'O número {n2} é o maior.')

else:
   print(f'O número {n3} é o maior.')

# Determinando o menor número.

if n < n2 and n < n3:
    print(f'O menor número é {n}.')

elif n2 < n and n2 < n3:
    print(f'O menor número é {n2}.')

else:
    print(f'O menor número é {n3}.')
