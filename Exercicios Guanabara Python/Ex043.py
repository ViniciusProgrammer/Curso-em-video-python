peso = float(input('Quanto você pesa? (Kg) '))
altura = float(input('Quanto de altura você tem? (m) '))
imc = peso / (altura**2)
print('O seu índice de massa corporal é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está com o PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está na faixa das pessoas com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA')
