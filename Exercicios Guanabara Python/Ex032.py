# Conferindo se o ano é BISSEXTO ou NÃO
ano = int(input('Qual o ano que você deseja analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))

#PARA SABER SE UM ANO É BISSEXTO BASTA
#1° SABER SE ELE É DIVISÍVEL POR 4 E O RESTO DA DIVISÃO DER 0
#2° SABER SE O RESTO DA DIVISÃO DELE POR 100 FOR DIFERENTE DE 0
#3° OU SE O RESTO DA DIVISÃO DELE POR 400 DER 0 TAMBÉM
