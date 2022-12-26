print('{:=^30}'.format(' VINICIUS STORE '))
valor = float(input('Qual o valor das suas compras? R$'))
print('''Nossas formas de pagamentos são essas:
[1] Pagamento no Dinheiro/Cheque (A VISTA)
[2] Pagamento em 1x no Cartão (A VISTA)
[3] Pagamento em 2x no Cartão
[4] Pagamento em 3x ou mais no Cartão''')
opção = int(input('Opção selecionada foi: '))
if opção == 1:
    print('Como você irá pagar suas compras no dinheiro, temos um desconto para você')
    print('Você irá pagar R${}'.format(valor * (90/100)))
elif opção == 2:
    print('Você selecionou a opção de pagamento em 1x no cartão')
    print('Você irá pagar no total R${}'.format(valor * (95/100)))
elif opção == 3:
    print('Você selecionou a opção de pagamento em 2x no cartão')
    print('Você irá pagar no total R${}'.format(valor))
else:
    print('Você selecionou a opção de pagamento em acima de 3x')
    print('Você pagará no total {}'.format(valor * (120/100)))
