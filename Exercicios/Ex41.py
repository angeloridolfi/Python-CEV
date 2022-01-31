from datetime import date

print(f"{'=-' * 3}DETERMINADOR DE CATEGORIA!{'=-' * 3}")

anasc = int(input('\n\033[34mDIGITE O ANO DO SEU NASCIMENTO:- \033[m'))
atual = date.today().year
idade = atual - anasc

if idade <= 9:
    print(f'\nVocê tem {idade} anos!')
    print(f'CATEGORIA: \033[43mMIRIM!\033[m')

elif 9 < idade <=14:
    print(f'\nVocê tem {idade} anos!')
    print("CATEGORIA: \033[42mINFANTIL\033[m")

elif 19 >= idade > 14:
    print(f'\nVocê tem {idade} anos!')
    print("CATEGORIA: \033[44mJUNIOR!\033[m")

elif 20 >= idade > 19:
    print(f'\nVocê tem {idade} anos!')
    print("CATEGORIA: \033[46mSÊNIOR!\033[m")

else:
    print(f'\nVocê tem {idade} anos!')
    print("CATEGORIA: \033[41mMASTER\033[m")