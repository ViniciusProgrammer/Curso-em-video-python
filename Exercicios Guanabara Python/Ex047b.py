#Se colocor qualquer número inteiro ele sempre pulará de 2 em 2 independentemente se for par ou impar
inicio = int(input(' Digite um número que você quer iniciar: '))
for c in range(inicio + 1, 51, 2):
    print(c)
print('---FIM---')
