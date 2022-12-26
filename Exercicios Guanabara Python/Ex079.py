valores = []

while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('O valor informado já foi adicionado, então não pode ser novamente adicionado!')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    perg = input('Quer coninuar [S/N]: ')
    if perg in 'Nn':
        valores.sort()
        print(f'Os valores digitados foram {valores}')
        break
    