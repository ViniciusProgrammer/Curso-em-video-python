seg1 = float(input('Qual o comprimento do seguimento 1? '))
seg2 = float(input('Qual o comprimento do seguimento 2? '))
seg3 = float(input('Qual o comprimento do seguimento 3? '))
if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('Podemos formar um triângulo!')
else:
    print('Não podemos formar um triângulo!') 
