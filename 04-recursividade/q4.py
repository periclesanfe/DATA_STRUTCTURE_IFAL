# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem crescente.


def printto(n):
    if n == 0:
        return 0
    else:
        return str(printto(n - 1)) + " " + str(n)


print(printto(int(input())))
