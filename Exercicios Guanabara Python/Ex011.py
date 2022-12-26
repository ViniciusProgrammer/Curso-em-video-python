#Quantidade de tinta para se pintar uma parede
largura = float(input('Qual a largura da parede em (m)? '))
altura = float(input('Qual a altura da parede em (m)? '))
area = (largura * altura)
tinta = (area / 2)
print('Para os {:.2f}m² das paredes a quantidade de litros de tinta necessária é {:.2f}L'.format(area, tinta))
