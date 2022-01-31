while True:
    n = int(input('Quer ver a tabuada de qual valor(Digite um número negativo para sair!): '))
    if n < 0:
        break
    print(f"{'=-' * 5} TABUADA DO {n} {'=-' * 5}")
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n * c}.')
        c += 1
    print('=-' * 13)
print('Finalizado!')
