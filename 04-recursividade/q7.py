# Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número. O
# fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15


def fatorialduplo(n):
    if n <= 0:
        return 1
    else:
        return n * fatorialduplo(n - 2)


# testes
resultado1 = fatorialduplo(5)
print(f"Fatorial duplo de 5: {resultado1}")

resultado2 = fatorialduplo(10)
print(f"Fatorial duplo de 10: {resultado2}")

resultado2 = fatorialduplo(3)
print(f"Fatorial duplo de 3: {resultado2}")

resultado2 = fatorialduplo(12)
print(f"Fatorial duplo de 12: {resultado2}")

resultado2 = fatorialduplo(20)
print(f"Fatorial duplo de 20: {resultado2}")
