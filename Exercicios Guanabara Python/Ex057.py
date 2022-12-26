sexo = str(input('Informe o seu Sexo, [M,F] ')).strip().upper()[0]
print(sexo)
while sexo not in 'Mm,Ff':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo [M,F] ')).strip().upper()[0]
print(f'Sexo {sexo}, informado com Sucesso')
