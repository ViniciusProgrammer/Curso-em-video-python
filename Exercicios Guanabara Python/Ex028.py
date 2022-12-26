#Tentando advinhar o que a máquina está pensando
import random, time
print('Vou tentar acertar o número que você pensou! ')
num = int(input('Acho que você pensou nesse número: '))
computador = random.randint(0, 5)
print('PROCESSANDO...')
time.sleep(2)
print('O número que eu pensei foi {}'.format(computador))
if num == computador:
    print('PARABÉNS, Você conseguiu me Vencer!')
else:
    print('Não foi dessa vez, jogador, por que eu pensei no {} e não no {}'.format(computador, num))
