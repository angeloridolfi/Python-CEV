contmaior = 0
contahomi = 0
contamuie = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('=-' * 19)
    idade = int(input('INFORME SUA IDADE: '))
    if idade > 18:
        contmaior += 1
    sexo = str(input('INFORME SEU SEXO <<M/F>>: ')).upper().strip()[0]
    if sexo not in 'MF':
        while True:
            sexo = str(input('OPÇÃO INVÁLIDA! INFORME SEU SEXO <<M/F>>: ')).upper().strip()[0]
            if sexo in 'MF':
                break
    if sexo == 'M':
        contahomi += 1
    if sexo == 'F' and idade < 20:
        contamuie += 1
    continuacao = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    print('=-' * 20)
    if continuacao not in 'SN':
        while True:
            continuacao = str(input('OPÇÃO INVÁLIDA! Quer continuar[S/N]: ')).upper().strip()[0]
            if continuacao in 'SN':
                break
    if continuacao == 'N':
        break
    print('=-' * 20)
print(f' -> {contmaior} pessoas são maiores de 18 anos;')
print(f' -> {contahomi} homens foram cadastrados;')
print(f' -> {contamuie} mulheres são menores de 20 anos.')
