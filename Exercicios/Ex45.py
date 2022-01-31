from random import randint
from time import sleep
#Fazendo o computador escolher ===>

list = ['','Pedra','Papel','Tesoura']
computador = randint(1,3)

print("""
\033[30;43m<= ESCOLHA QUAL DESSE VOCÊ QUER =>\033[m]
\033[32m================
| 1 - Pedra.   |
| 2 - Papel.   |
| 3 - Tesoura. |
================\033[m""")

jog = int(input("Escolha qual das alternativas você quer[1, 2, 3]: "))

#Efeito JoKenPo!

print("\033[32mJO\033[m")
sleep(1)
print("\033[31mKEN\033[m")
sleep(1)
print("\033[33mPO!!!\033[m")
sleep(0.5)

if computador == 1:
    if jog == 1:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[33mEMPATE!\033[m")
    elif jog == 2:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[32mPARÁBENS!!! VOCÊ VENCEU!")
    elif jog == 3:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[31mVOCÊ PERDEU!\033[m")

if computador == 2:
    if jog == 1:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[31mVOCÊ PERDEU!\033[m")
    elif jog == 2:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[33mEMPATE!\033[m")
    elif jog == 3:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[32mPARÁBENS!!! VOCÊ VENCEU!\033[m")
if computador == 3:
    if jog == 1:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[32mPARÁBENS!!! VOCÊ VENCEU!")
    elif jog == 2:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[31mVOCẼ PERDEU!\033[m")
    elif jog == 3:
        print(f"O computador escolheu {list[computador]} e você escolheu {list[jog]}!")
        print("\033[33mEMPATE!!\033[m")
