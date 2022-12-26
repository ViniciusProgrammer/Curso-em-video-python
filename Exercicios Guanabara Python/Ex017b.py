#Calculando a hipotenusa através da biblioteca math com a função hypot
from math import hypot
cateto_oposto = float(input('O comprimento do cateto oposto: '))
cateto_adjascente = float(input('O comprimento do cateto adjascente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjascente)
print('A Hipotenusa vale {}'.format(hipotenusa))
