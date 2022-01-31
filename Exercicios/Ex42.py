print(f"\033[30;43m{'=-' * 4}TRIÃNGULOS{'=-' * 4}\033[m")

###Coletando informações das retas!

reta1 = float(input('DIGITE O VALOR DA PRIMEIRA RETA:- '))
reta2 = float(input('DIGITE O VALOR DA SEGUNDA RETA:- '))
reta3 = float(input('DIGITE O VALOR DA TERCEIRA RETA:- '))

#Diagnosticando se pode formar um triângulo!

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print('\033[42mESSAS RETAS PODEM FORMAR UM TRIÃNGULO!\033[m')
    
    if reta2 == reta1 == reta3:
        print(f"\n\033[45mESSE TRIANGULO É UM TRIÂNGULO EQUILÁTERO!\033[m")

    elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta3 == reta1 != reta2:
        print("\n\033[46mESSE TRIÂNGULO É UM TRIÂNGULO ISÓSCELES!\033[m")

    elif reta1 != reta2 != reta3:
        print("\n\033[42mESSE TRIÂNGULO É UM TRIÃNGULO ESCALENO!\033[m")


else:
    print('\033[41mESSAS RETAS NÃO PODEM FORMAR UM TRIÂNGULO!\033[m')
