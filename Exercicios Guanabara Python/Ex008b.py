#Convertendo medidas sem variaveis
medida = float(input('Digite o comprimento em metros: '))
print('A medida de {}m equivale a {}dcm, a {}cm e {}mm'.format(medida, (medida*10), (medida*100), (medida*1000)))
print('A medida de {}m equivale a {}dam, a {}hm e a {}km'.format(medida, (medida/10), (medida/100), (medida/1000)))
