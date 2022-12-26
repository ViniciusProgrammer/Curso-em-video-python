#Mostrando o dobro, o triplo e a raiz quadrada de um número
num = int(input('Digite um valor: '))
dobro = (num * 2)
triplo = (num * 3)
raiz = (num ** (1/2))
print('O dobro do {}, vale {} \nO seu trplo vale {} \nA sua raíz vale {:.1f}'.format(num, dobro, triplo, raiz))
