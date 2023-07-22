# Faça uma função maior_de_2(num1, num2) que, dados dois numeros, retorna o maior deles.

def maior_de_2(num1, num2):
    return num1 if num1 > num2 else num2


#teste
print(maior_de_2(1, 2))
print(maior_de_2(-1, 2))
print(maior_de_2(10, 2))
print(maior_de_2(0, 0)) 
