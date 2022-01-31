s = 0
co = 0
ida = 0
for c in range(1, 5):
    print(f"{'=-' * 5}{c}ª pessoa{'=-' * 5}")
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo: [M / F]')).lower()
    s += idade
    if idade > ida and sexo == 'm':
        ido = nome
        ida = idade
    elif idade < 20 and sexo == 'f':
        co += 1
media = s / 4
print(f'Á média de idade de todo o grupo é de {media}')
print(f'O homem mais velho é o {ido}, com {ida} anos.')
print(f'No total, {co} mulher/es tem menos de 20 anos!')
