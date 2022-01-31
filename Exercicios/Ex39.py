from datetime import date

print(f"\033[32m{'#' * 3}ALISTAMENTO{'#' * 3}\033[m")
ano = int(input('Digite o ano em que você nasceu:- '))
atual = date.today().year

print(f'Levando em consideração que estamos no ano de {atual}')

calc = atual - ano

if calc == 18:
    print(f"Você já está, ou irá fazer {calc} anos!")
    print('\033[30;43mESTÁ NA HORA DE SE ALISTAR PARA SERVIR O SEU PÁIS!\033[m')
elif calc > 18:
    print(f"Você já está, ou irá fazer {calc} anos!")
    print('\033[30;41mJá passou da hora de fazer o seu alistamento!\033[m')
else:
    print(f"Você já está, ou irá fazer {calc} anos!")
    print('\033[42;30mAinda não está na hora de fazer o seu alistamento!\033[m')