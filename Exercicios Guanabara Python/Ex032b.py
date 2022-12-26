#Vendo se o ano atual é BISSEXTO utilizando também o ano atual da máquina
from datetime import date
ano = int(input('Qual o ano que você quer analisar? Se o ano qeu você quer for o atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))
