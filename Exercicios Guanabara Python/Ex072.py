from time import sleep
valor = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou {valor[num]}')
        break
    else:
        print('Você mão digitou um número entre 0 e 20. Tente Novamente!')
print('Estamos finalizando...')
sleep(2)
