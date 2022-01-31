frase = str(input('Digite uma frase:')).strip().upper()
cont = frase.count('A')

print(f'Na sua frase, aparece {cont} vezes a letra A!')
print('A letra A aparece primeiro na posição {} e por ultimo na posição {}'.format(frase.find('A')+1, frase.rfind('A')+1))
