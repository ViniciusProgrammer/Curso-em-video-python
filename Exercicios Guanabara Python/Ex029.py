#Calculando a multa a ser paga em caso de infração
velocidade = float(input('Qual a velocidade do veículo ao passar pelo radar? Km '))
print('Você está andando a {}Km/h'.format(velocidade))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Muito bem, você está dentro dos parãmetros de velocidade da vida, continue assim!!')
else:
    print('Opa, você excedeu os limites de velocidade da via, você pagará multa no valor de {}'.format(multa))
