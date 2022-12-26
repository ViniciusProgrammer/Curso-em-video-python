casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Quanto que você ganha? R$ '))
anos = int(input('Em quantos anos você quer quitar a casa? '))
prestação = casa / (anos * 12)
máximo = salário * 30/100
print('Para pagar uma casa no valor de R${} é preciso pagar parcelas no valor de {:.2f}'.format(casa, prestação))
if prestação <= máximo:
    print('Parabéns, o seu empréstimo foi APROVADO!!')
else:
    print('A sua solicitação de empréstimo foi NEGADA!')
