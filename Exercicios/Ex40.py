print(f"\033[33m{'=-' * 3}VERIFICADOR DE MÉDIA{'-=' * 3}\033[m")

nota1 = float(input('DIGITE A PRIMEIRA NOTA DO ALUNO:- '))
nota2 = float(input('DIGITE A SEGUNDA NOTA DO ALUNO:- '))


md = ((nota1 + nota2) / 2)

if md < 5.0:
    print(f'SUA MÉDIA É DE {md:.1f}, que está abaixo de 5.0!')
    print('SITUAÇÃO: \033[41mREPROVADO!\033[m')

elif 5 <= md and md <= 6.9:
    print(f'Sua média de {md:.1f} está entre 5 e 6.9!')
    print('Situação: \033[43mEM RECUPERAÇÃO!\033[m')

else:
    print(f'Sua média foi de {md:.1f}!')
    print(f'Situação: \033[42mAPROVADO!\033[m')
