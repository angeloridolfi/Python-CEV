# Coletando o valor do salário.

sal = float(input('Informe o salário do funcionário:'))

# Cálculos a respeito do aumento.

if sal > 1250:
    # Calculando porcentagem do valor total do salário.
    calc = (sal * 10) / 100

else:
    # ^^
    calc = (sal * 15) / 100

print(f'O salário de R${sal}, fica, com o aumento, no total de R${sal + calc}.')
