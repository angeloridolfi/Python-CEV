from datetime import date

ano = int(input('Digite um ano e verificaremos se ele é bissexto: \nColoque 0 para análisar o ano atual: \n'))

if ano == 0:
    ano = date.today().year


if (ano % 4 == 0) and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} Não é bissexto:')
