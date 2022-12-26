nome = str(input("Digite o seu nome completo: ")).strip()
print(nome.upper()) # mostra nome em maiusculo
print(nome.lower()) # mostra nome em minusculo
print(nome.replace(" ", "")) # remove todos os espaços na string
print('O seu primeiro nome tem {} letras'.format(len(nome[0:8])))
print('O seu nome tem ao todo {} contando também os espaços'.format(len(nome)))
print('O seu nome ao todo tem {} letras sem considerar os espaços'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

