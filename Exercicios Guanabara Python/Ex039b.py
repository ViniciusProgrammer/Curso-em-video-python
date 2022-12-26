from datetime import date
atual = date.today().year
nascimento = int(input('Qual foi o ano do seu nascimento? '))
idade = atual - nascimento
print('''Me informe o seu Sexo:
[1] Sou do Sexo MASCULINO
[2] Sou do sexo FEMININO''')
opção = int(input('Sua opção foi: '))
if opção == 1:
    print('Você é do Sexo masculino, portanto é seu dever se ALISTAR')
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem idade para se alistar ')
    saldo = 18 - idade
    print('Ainda falta {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('O seu alistamento será em {}'.format(ano))
elif idade > 18:
    print('Você já passou do período para se alistar')
    saldo = 18 + idade
    print('Voce deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('O ano do seu alistamento foi em {}'.format(ano))
elif opção == 2:
    print('Você é do sexo FEMININO, portanto não precisa se alistar!')
