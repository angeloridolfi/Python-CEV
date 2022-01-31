
sexo = str(input('Qual seu sexo: [M/F]')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Digite corretamente o seu sexo: [M/F]')).upper()
print(f'Sexo {sexo} registrado!')

