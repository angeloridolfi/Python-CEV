from time import sleep
vel = float(input('Digite a velocidade de um carro: '))

print('Analisando a sua velocidade...')
sleep(2)

if vel > 80.0: # Calculando Multa<--
    print('A sua velocidade ultrapassou o limite de 80 km/h, você foi multado em R${}'.format(7*(vel-80)))

print('A sua velocidade está dentro do limite permitido. Boa viagem!')
