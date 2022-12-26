#Calculando o seno, cosseno e tangente do angulo mostrado
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {:.2f} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
