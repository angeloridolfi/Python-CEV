from random import randint
from time import sleep
n = randint(0, 5)

print("""
O computador vai selecionar um número de 0 a 5;
Vamos ver se você consegue adivinhar?""")

alt = int(input('Vai lá, escolha um número de 0 a 5:'))
print("Processando...")
sleep(3.5)
if alt == n:
    print(f'Parábens, o computador escolheu o número {n} e você acertou!!! =D')

else:
    print(f'Aaah, que pena. O computador escolheu {n} e você escolheu {alt}. Você errou!\nTente novamente.')
