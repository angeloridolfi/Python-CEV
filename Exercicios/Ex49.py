n = int(input('Digite um número para ver sua tabuada: '))
print(f"{'=-' * 5}Tabuada do {n}{'=-' * 5}")
for c in range(1, 11):
    print(f'{n} x {c} == {n * c}')
print('=-' * 10)
print('FIM')
