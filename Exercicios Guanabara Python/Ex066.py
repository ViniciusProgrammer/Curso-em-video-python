contador = 0 
soma = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    contador = contador + 1
    soma = soma + num
print(f'Foram digitados {contador} números e a soma deles foi igual a {soma}')
