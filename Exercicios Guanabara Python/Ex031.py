#Custo de uma viagem
distancia = float(input('Quantos quilômetros rodados? '))
valor1 = distancia * 0.5
valor2 = distancia * 0.45
if distancia <= 200:
    print('O valor a ser pago pela distância de {} é R${:.2f}'.format(distancia, valor1))
else: 
    print('O valor a ser pago pela distância de {} é R${:.2f}'.format(distancia, valor2))
