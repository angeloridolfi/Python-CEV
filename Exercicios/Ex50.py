s = 0
co = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro(IREMOS SOMAR SOMENTE OS PARES!): '))
    if num % 2 == 0:
        s += num
        co += 1
print(f"Você informou {co} números pares, e sua soma é igual a {s}!")
