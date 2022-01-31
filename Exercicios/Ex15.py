km = float(input('Qual a quantidade de KM rodados com o carro? : '))
d = int(input('Qual a quantidade de dias rodados com o carro? : '))

print(f'Como o carro percorreu {km}km e foi alugado por {d} dias, o valor total do aluguel será de:\n R${60*d+0.15*km:.2f}')
