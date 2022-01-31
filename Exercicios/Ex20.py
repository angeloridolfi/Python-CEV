from random import shuffle
from typing import List

n = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista: list[str] = [n, n2, n3, n4]
shuffle(lista)
print(f'Dentre os alunos apresentados, {n}, {n2}, {n3} e {n4}. A ordem sorteada é {lista}')
