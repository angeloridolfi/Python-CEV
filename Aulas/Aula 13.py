# Laços de repetição!
# Estrutura de repetição "for"...

# for c in range(6, 0, -1):
#    print(c)

#from time import sleep
#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#    sleep(1)
#print('fim')

#i = int(input('Digite o número que vocẽ desja começar a contagem: '))
#f = int(input('Até quanto você quer que a contagem vá: '))
#p = int(input('De quanto em quanto: '))

#for c in range(i, f+1, p):
#   print(c)
#    sleep(0.7)
#print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor!'))
    s += n
print(f'Soma = {s}')