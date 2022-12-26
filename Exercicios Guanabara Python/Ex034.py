salário = float(input('Qual o seu salário atual? R$'))
if salário > 1250:
    aumento = salário * 110/100
    print('O seu novo salário passará a ser R${}'.format(aumento))
else:
    aumento = salário * 115/100
    print('O seu novo saário será de R$ {}'.format(aumento))
