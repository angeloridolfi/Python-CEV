print(f"\033[33m{'=-' * 4}IMC{'=-' * 4}\033[m")

#Recolhendo as informações do paciente!

peso = float(input("DIGITE O SEU PESO [EM KG]:- "))
altura = float(input("DIGITE SUA ALTURA [EM CM!]:- "))

# Cálculo do IMC!

imc = (peso / ((altura / 100) * (altura / 100)))

print(f"O valor do seu IMC é igual a: {imc:.1f}kg/m^2")

#Determinando as condições do seu corpo de acordo com os cálculos!

if imc < 18.5:
    print("\033[30;43mVocê esta ABAIXO DO PESO!\033[m")
elif 18.5 <= imc < 25:
    print("\033[30;42mVocê está com o PESO IDEAL!\033[m")
elif 25 <= imc < 30:
    print("\033[30;43mVocê esta com SOBREPESO! Cuidado!\033[m")
elif 30 <= imc < 40:
    print("\033[30;41mVocê está em estado de OBESIDADE!\033[m")
else:
    print("\033[41mOBESIDADE MÓRBIDA! PROCURE UM ESPECIALISTA!\033[m")
