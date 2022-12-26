nota1 = float(input('Qual foi a sua primeira NOTA?' ))
nota2 = float(input('Qual foi a sua Segunda NOTA? '))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Parabéns, você está APROVADO!')
elif média >= 5 and média <= 6.9:
    print('Opa, você precisa fazer RECUPERAÇÃO')
elif média < 5:
    print('Você está REPROVADO')
