num = int(input('Me informe um número qualquer: '))
print('O número informado por você foi {}'.format(num))
resultado = num % 2
if resultado == 0:
    print('O número {} analisado é PAR'.format(num))
else:
    print('O número {} analisado é IMPAR'.format(num))
