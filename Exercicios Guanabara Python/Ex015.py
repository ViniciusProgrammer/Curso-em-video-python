#Aluguel de carros
distancia = float(input('Quantos quilometros foi o percurso? Km '))
dias = int(input('Quantos dias o carro ficou alugado? '))
total = (dias * 60) + (distancia * 0.15)
print('O total a ser pago pela alocação do carro será {}'.format(total))
