from datetime import date
nascimento = int(input('Digite o seu ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('O atleta tem {} anos de idade'.format(idade))
if idade <= 9:
    print('O atleta pertence a categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta pertence a categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('O atleta pertence a categoria JÚNIOR')
elif idade > 19 and idade <= 25:
    print('O atleta pertence a categoria SÊNIOR')
elif idade > 25:
    print('O atleta pertence a categoria MASTER')
