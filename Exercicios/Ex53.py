print('PALINDROMO')

frase = str(input('Digite uma frase para verificarmos se é um palindromo: ')).strip().upper().split()
junto = ''.join(frase)
con = junto[:: -1]

# Inverter com o laço for: ==>
###for letra in range(len(junto) - 1, -1, -1):
    ###con += junto[letra]
print(f'A frase {junto} ao contrário fica: {con}')
if junto == con:
    print('Sua frase é um PALINDROMO!')
else:
    print('Sua frase não é um palindromo!')
