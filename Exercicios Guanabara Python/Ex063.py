num = int(input('Digite quantos termos você quer mostrar: '))
primeiro_termo = 0
segundo_termo = 1
contador = 3
print('{} -> {}'.format(primeiro_termo, segundo_termo), end='')
while contador <= num:
    terceiro_termo = primeiro_termo + segundo_termo
    print(' -> {}'.format(terceiro_termo), end='')
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador = contador + 1
print(' -> FIM')
