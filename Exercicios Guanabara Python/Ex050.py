soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor inteiro: '))
    if c % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você me informou {} PARES e a soma entre os números solicitados foi {}'.format(cont, soma))
