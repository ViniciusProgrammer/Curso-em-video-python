#Fazendo um ordem de apresentação de um trabalho
import random
aluno_1 = str(input('Nome do primeiro aluno: '))
aluno_2 = str(input('Nome do segundo aluno: '))
aluno_3 = str(input('Nome do terceiro aluno: '))
aluno_4 = str(input('Nome do quarto aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista)
print('A ordem da apresentação será')
print(lista)
