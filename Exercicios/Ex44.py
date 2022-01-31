print(f"\033[41;30m{'=-' * 3}CONDIÇÕES DE PAGAMENTO!{'=-' * 3}\033[m")

#Coletando o valor do produto!

pre = float(input('\nDIGITE O VALOR DO PRODUTO:-R$'))

#Apresentando as opções de pagamento!

print("""\n
          \033[33mOPÇÕES DE PAGAMENTO\033m
\033[32m###########################################
# 1 - à vista[10% de desconto]!           #
#                                         #
# 2 - à vista no cartão[5% de desconto]   #
#                                         #
# 3 - em até 2x no cartão[preço normal]   #
#                                         #
# 4 - 3x ou mais no cartão [20% de juros] #
###########################################\033[m""")

#Deixando o cliente escolher o meio de pagamento ==>
op = str(input('\nDIGITE QUAL VAI SER O MEIO DE PAGAMENTO[1, 2, 3 OU 4]: '))

# Lidando com os meios de pagamento ===>

if op == '1':
    desc = pre - ((pre * 10) / 100)
    print(f"\nO preço a ser pago pelo produto, com 10% de desconto, é igual a: R${desc:.2f}")
elif op == '2':
    desc = pre - ((pre * 5) / 100)
    print(f"\nO preço a ser pago pelo produto, com 5% de desconto é igual a: RS{desc:.2f}")
elif op == '3':
    print(f'O preço em 2x no cartão continua com o valor de R${pre:.2f}')
elif op == '4':
    jur = pre + ((pre * 20) / 100)
    print(f'O preço em 3x ou mais no cartão, com 20% de juros é igual a: R${jur:.2f}')
else:
    print(f'\033[41mOPÇÃO INVÁLIDA!\033[m')
