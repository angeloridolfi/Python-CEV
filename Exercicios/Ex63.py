n = int(input('Digite até qual elemento da sequẽncia fibonacci vocẽ quer ver: '))
p = 0
s = 1
cont = 0
print(f'Os {n} primeiros termos Fibonacci são:')
while cont != n:
    ter = p + s
    print(p, end=' -> ')
    p = s
    s = ter
    cont += 1
print('FIM!')
    