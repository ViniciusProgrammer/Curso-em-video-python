num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções abaixo:
[1] Converta para BINÁRIO
[2] Converta para OCTAL
[3] Converta para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA, tente novamente!')
