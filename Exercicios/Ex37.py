
num = int(input('\n\033[33mDigite um número inteiro qualquer: \033[m'))

print(f"""
ESCOLHA EM QUAL DESSAS BASE VOCÊ QUER QUE CONVERTA O NÚMERO:
            \033[32m###################
            #                 #    
            # 1 - BINÁRIO     #
            #                 #
            # 2 - Octal       #
            #                 #
            # 3 - Hexadecimal #
            #                 #
            ###################\033[m""")

esc = str(input('\033[30;43mDigite a opção desejada(1,2 ou 3):-\033[m'))

if esc == "1":
    bina = bin(num)
    print(f'O número \033[34m{num}\033[m em \033[30;42mBINÁRIO\033[m fica: \033[32m{bina}\033[m')

elif esc == "2":
    octo = oct(num)
    print(f'O número \033[34m{num}\033[m em \033[30;42mOCTAL\033[m fica: \033[32m{octo}\033[m')

elif esc == "3":
    he = hex(num)
    print(f'O número \033[34m{num}\033[m em \033[30;42mOCTAL\033[m fica: \033[32m{he}\033[m')

else:
    print('\033[30;41mOPÇÃO INVÁLIDA!\033[m')
