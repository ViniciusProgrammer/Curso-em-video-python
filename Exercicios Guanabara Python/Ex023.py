num = int(input('Digite um valor entre 0 e 9999: '))
print(num)
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('A unidade é {}'.format(unidade))
print('A dezena é {}'.format(dezena))
print('A centena é {}'.format(centena))
print('A milhar vale {}'.format(milhar))
