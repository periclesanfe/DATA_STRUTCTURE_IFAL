# Faça uma função fatorial(n) que, dado um numero N, calcule e retorne o fatorial de N. O fatorial de um número natural n, representado por N!, é o produto de todos os inteiros positivos menores ou iguais a n. exemplo: 5! = 5*4*3*2*1 = 120

def fatorial(n):
    res = 1
    while n != 0:
        res = res * n
        n -= 1
    return res

# TESTE
print(fatorial(6))
print(fatorial(5))
print(fatorial(4))
print(fatorial(3))
print(fatorial(2))
print(fatorial(1))
