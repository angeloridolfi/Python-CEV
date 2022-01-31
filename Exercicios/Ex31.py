km = float(input('Digite a distância da sua viagem: '))

if km <= 200:
    print(f'Como a sua viagem é de {km} o preço da sua passagem será R${0.5*km}')

else:
    print(f'Como a sua viagem é mais longa que 200km, o preço da sua passagem sera de R${0.45*km}')
print('Boa Viagem!')
