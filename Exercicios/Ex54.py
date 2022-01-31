from datetime import date
atual = date.today().year
s1 = 0
s2 = 0
for cont in range(1, 8):
    ano = int(input('Digite o ano do seu nascimento: '))
    ida = atual - ano
    if ida >= 21:
        s1 += 1
    else:
        s2 += 1
print(f'Dentre as {cont} pessoas, {s1} completaram a maioridade!')
print(f'E {s2} ainda são menores de idade!')
