from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano em que você nasceu? '))
idade = atual - nascimento
print('Quem nasceu no ano de {} tem hoje {} anos'.format(nascimento, idade))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem idade para se alistar') 
    saldo = 18 - idade
    print('Ainda faltam {} anos para você poder se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    print('Você já deveria ter se alistado')
    saldo = idade - 18
    print('O período em que você deveria ter se alistado deveria ser feito há {} anos'.format(saldo))
    ano = atual - saldo
    print('O seu alistamento foi em {}'.format(ano))
    