# 7. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).


def epar(num):
    if num % 2 == 0:
        return f"O número {num} é par"
    return f"O número {num} não é par"


print(epar(int(input("Digite um número: "))))
