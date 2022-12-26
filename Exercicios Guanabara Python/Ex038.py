num1 = int(input('Digite um primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro número é MAIOR do que o segundo número')  
elif num2 > num1:
    print('O segundo número é MAIOR do que o primeiro número')
else:
    print('Não existe número maior que o outro pois {} é igual a {}'.format(num1, num2))
