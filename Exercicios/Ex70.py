tot = barato = contamil = contador = 0
baratonome = ''
while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$'))
    contador += 1
    if contador == 1 or preco < barato:
        barato = preco
        baratonome = nome
    tot += preco
    if preco > 1000:
        contamil += 1
    esc = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    print('=-' * 20)
    if esc not in 'SN':
        while True:
            esc = str(input('OPÇÃO INVÁLIDA! Deseja continuar: [S/N] ')).strip().upper()[0]
            if esc in 'SN':
                break
    elif esc == 'N':
        break

print(f'O total gasto na compra foi de: R${tot:.2f}')
print(f'{contamil} produtos custaram mais de R$1000.00.')
print(f'O produto mais barato foi: {baratonome}, com o valor de R${barato:.2f}.')
