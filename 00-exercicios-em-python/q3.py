# Calcule o fatorial de um numero qualquer.
# O fatorial de um numero n é o n*(n-1)*(n-2)*...*1


def calc_fat(n):
    fatorial = 1
    while n != 1:
        fatorial *= n
        n -= 1
    print(fatorial)


calc_fat(int(input("Digite um numero: ")))
