from time import sleep
print(f"\033[30;43m{'#' * 4}COMPARADOR DE NÚMEROS INTEIROS{'#' * 4}\033[m")

n1 = int(input('\033[32m#DIGITE O PRIMEIRO NÚMERO:- '))
n2 = int(input('#DIGITE O SEGUNDO NÚMERO:- '))
print("\033[m")
print("""
      III
      III
      III
    VVVVVVV
     VVVVV
      VVV
       V   """)
print('Analisando os números...')

sleep(3)

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}.')

elif n1 < n2:
    print(f'O número {n2} é maior que o número {n1}.')

else:
    print(f'Os números {n1} e {n2}, são iguais!')
