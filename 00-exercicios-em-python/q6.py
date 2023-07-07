# Escreva um programa que utiliza a função da questão 5 para alterar x
# O programa deve parar quando x tiver o valor final de 1
# por exemplo, para x=13 o resultado é:
# 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


def muda_x(x):
    if x % 2 == 0:
        return int(x / 2)
    return int(3 * x + 1)


x = int(input())
output = ""
while x != 1:
    x = muda_x(x)
    if x == 1:
        output += str(x)
        continue
    output += str(x) + " -> "
print(output)
