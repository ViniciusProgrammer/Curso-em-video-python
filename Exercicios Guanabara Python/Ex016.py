#arredondamentos de números
from math import trunc, floor, ceil
num = float(input('Digite um número: '))
inteira = trunc(num)
print('A parte inteira de {} é {}'.format(num, inteira))
print('Arredondando {} para cima temos {}'.format(num, ceil(num)))
print('Arredondando {} para baixo temos {}'.format(num, floor(num)))
