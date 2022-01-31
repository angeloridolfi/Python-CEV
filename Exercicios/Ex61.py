print('P.A')

primeiro = int(input('Digite o primeiro termo de uma p.A: '))
raz = int(input('Digite a razão da p.a: '))
dec = primeiro + (10 - 1) * raz

while primeiro != (dec + raz):
    print(primeiro,end=' - ')
    primeiro += raz
print('Fim!')