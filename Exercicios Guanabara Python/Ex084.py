pessoas = []
pesadas = []
leves = []
while True:
    nome = str(input('Informe o seu nome: '))
    peso = float(input('Qual o seu peso em (Kg): '))
    pessoas.append(nome)
    if peso <= 80:
        leves.append(f'{nome} Com {peso}Kg')
    elif peso > 80 and peso <= 120:
        pesadas.append(f'{nome} Com {peso} Kg')
    else:
        break
print('Você cadastrou {} pessoas no total'.format(len(pessoas)))
print(f'Os mais pesados encontrados na lista foram {pesadas}')
print(f'Os mais leves foram {leves} ')
