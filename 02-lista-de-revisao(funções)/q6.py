# Faça uma função maior_de_3(num1, num2, num3) que, dados três numeros, retorna a maior deles

def maior_de_3(num1, num2, num3):
    lista = [num1, num2, num3]
    return max(lista)


#testes
print(maior_de_3(int(input()), int(input()), int(input())))
print(maior_de_3(1,2,3))
print(maior_de_3(10,2,3))
print(maior_de_3(0,0,0))
print(maior_de_3(1,25,3))
