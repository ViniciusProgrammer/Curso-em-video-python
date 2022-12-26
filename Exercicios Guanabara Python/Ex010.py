#Convertendo real para dólar e Euro
grana = float(input('Quantos reais você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(grana, grana/5.26))
print('Com R${} você pode comprar £{:.2f}'.format(grana, grana/5.35))
