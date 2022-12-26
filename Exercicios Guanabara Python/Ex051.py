termo1 = int(input('Primeito termo: '))
razão = int(input('Digite a razão: '))
décimo = termo1 + (10 - 1) * razão
for c in range(termo1, décimo + razão, razão):
    print(c , end=' -> ')
print('ACABOU')
