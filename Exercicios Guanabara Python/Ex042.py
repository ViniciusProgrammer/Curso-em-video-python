seg1 = float(input('Comprimento do primeiro seguimento: '))
seg2 = float(input('Comprimento do segundo seguimento: '))
seg3 = float(input('Comprimento do terceiro seguimento: '))
if seg1 < (seg2 + seg2) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('Podemos formar um triângulo')
    if seg1 == seg2 and seg2 == seg3:
        print('De acordo com os seguimentos acima, podemos formar um triângulo EQUILÁTERO')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('De acordo com os segimentosa acima, podemos formar um triãngulo ISÓSCELES')
    elif seg1 != seg2 and seg2 != seg3 and seg1!= seg3:
        print('De acordo com os seguimentos acima, podemos formar um triângulo ESCALENO')
else:
    print('Não podemos formar nenhum triângulo com os seguimentos informados pelo Usuário!')
