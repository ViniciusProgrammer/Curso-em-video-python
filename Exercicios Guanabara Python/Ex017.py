#Calculando o comprimento da hipotenusa matematicamente
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjascente = float(input('Comprimento do cateto adjascente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjascente **2) ** (1/2)
print('O comprimento da hipotenusa é {}'.format(hipotenusa))
