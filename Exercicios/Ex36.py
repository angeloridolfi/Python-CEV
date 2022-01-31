print(f"\n\033[33m{'#'*5}CALCULADOR DE EMPRESTIMO!{'#'*5}\033[m\n")

valorcasa = float(input('Digite aqui o valor da sua casa: '))
sal = float(input('Informe-nos o valor do seu salário mensal: '))
tem = float(input('Em quantos anos você deseja pagar a sua casa: '))

pre = valorcasa / (tem * 12)
porc = (sal * 30) / 100

print(f'O valor da sua prestação será de {pre:.2f}')

if pre >= porc:
    print(f'\nO valor da sua prestação é maior que 30% do seu salário({porc:.2f})!')
    print(f'No entanto o seu empréstimo foi \033[30;41mNEGADO!\033[m')

else:
    print(f'\nO valor da sua prestação é menor que 30% do seu salário({porc:.2f})!')
    print(f'No entanto o seu empréstimo foi \033[30;42mAPROVADO!\033[m')

