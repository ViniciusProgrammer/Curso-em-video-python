from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}° nasceu? '.format(pessoa) ))
    idade = ano_atual - nascimento
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
