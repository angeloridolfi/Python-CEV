print('P.A')

primeiro = esc = int(input('Digite o primeiro termo de uma p.A: '))
raz = int(input('Digite a razão da p.a: '))
dec = primeiro + (10 - 1) * raz
cont = 0
print('\nOs dez primeiros termos são:')
while esc != 0:
    while primeiro != (dec + raz):
        print(primeiro,end=' - ')
        primeiro += raz
        cont += 1
    print('PAUSA')
    esc = int(input('\nQuer mostrar mais quantos termos: '))
    dec = primeiro + (esc -1) * raz
print(f'Foram mostrados no total {cont} termos!')
print('\nFim!')