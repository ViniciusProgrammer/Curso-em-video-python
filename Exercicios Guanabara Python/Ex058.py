import random
from time import sleep
tentativas = 1
print('Vou tentar advinhar o número que você pensou!')
jogador = int(input('Você pensou no número: '))
print('PROCESSANDO...')
sleep(2)
computador = random.randint(0, 10)
print(f'Eu pensei no número {computador}')
while jogador != computador:
    jogador = int(input('Número errado. Por favor, tente novamente: '))
    print('PROCESSANDO...')
    sleep(2)
    tentativas = tentativas + 1
if jogador == computador:
    print('Parabéns você me venceu!')
print(f'Foram necessárias {tentativas} para conseguir me vencer')
