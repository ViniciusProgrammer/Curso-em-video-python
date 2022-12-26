lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Informe um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Os valores digitados por você são {lista} ')
print(f'O maior valor digitado foi {maior}')
for i, v in enumerate(lista):
    if v == maior:
        print(f'O maior ou maiores valores {maior} foram digitados nas posições {i}...', end='')
print()
print(f'O menor valor digitado foi {menor}')
for i, v in enumerate(lista):
    if v == menor:
        print(f'O menor valor(s) {menor} foram digitados na(s) posições {i}...', end='')
print()
