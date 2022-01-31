from random import randint
computador = randint(1, 10)
tentativas = 0
acerto = False
while not acerto:
    jog = int(input('Digite um número de 1 a 10:'))
    tentativas += 1
    if jog == computador:
        acerto = True
    else:
        if jog < computador:
            print('Mais! Tente novamente!')
        else:
            print('Menos! Tente novamente!')
print(f'Você venceu! Foram necessárias {tentativas} tentativas para ganhar!')
print(f'O computador havia escolhido {computador}!')
