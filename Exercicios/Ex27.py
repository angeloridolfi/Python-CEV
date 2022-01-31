nome = str(input('Digite seu nome completo:'))
sepa = nome.split()
print(sepa)

print('primeiro nome = {}'.format(sepa[0]))
print('ultimo nome = {}'.format(sepa[len(sepa)-1]))
