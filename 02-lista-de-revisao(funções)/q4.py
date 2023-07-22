# Escreva uma função compare(a,b) que recebe dois numeros a e b como parametro e retorna 1 se a > b, 0 se a == b, e -1 se a < b.

def compare(a, b):
    if a > b:
        return '1'
    elif a == b:
        return '0'
    return '-1'


#teste
print(compare(6, 5))
print(compare(6, 6))
print(compare(4, 5))
