#Convertendo temperaturas
temperatura = float(input('Qual é a temperatura hoje? °C'))
convertendo = (temperatura * 1.8) + 32
print('Hoje está fazendo {}°C o que equivale em {:.1f}°F'.format(temperatura, convertendo))
