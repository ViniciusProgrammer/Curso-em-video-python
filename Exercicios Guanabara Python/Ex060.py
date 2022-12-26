#fatorial de um número
num = int(input('Digite um valor: '))
c = num
resultado = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado = resultado * c
    c = c - 1
print('{}'.format(resultado))
