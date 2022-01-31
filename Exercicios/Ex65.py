pro = 'S'
maior = menor = cont = soma = 0

while pro in 'sS':
        cont += 1
        num = int(input('Digite um número: '))
        if cont == 1:
            maior = menor = num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        soma += num
        pro = str(input('Quer digitar mais um[S / N]')).upper()
media = soma / cont
print(f'A média entre esses valores foi de {media}')
print(f'O maior número digitado foi: {maior} e o menor foi {menor}!')
print('FIM!')
