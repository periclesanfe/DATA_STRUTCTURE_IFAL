# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem decrescente.


def printto(n):
    if n == 0:
        return 0
    else:
        return str(n) + " " + str(printto(n - 1))


print(printto(int(input())))
