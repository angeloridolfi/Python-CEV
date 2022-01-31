from random import choice

n = input('Digite o nome do primeiro aluno:')
n2 = input('Digite o nome do segundo aluno:')
n3 = input('Digite o nome do terceiro aluno:')
n4 = input('Digite o nome do quarto aluno:')
lista = [n , n2, n3, n4]

print(f'Dentre os alunos {n}, {n2}, {n3} e {n4}. O sorteado foi o {choice(lista)}.')
