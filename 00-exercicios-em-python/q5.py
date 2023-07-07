# Escreva uma função em que, dada uma variavel x com algum valor inteiro,
# temos um novo x de acordo com a seguinte regra:
# Se x é par, x = x /
# Se X é impar, x = 3*x+1
# imprime X


def muda_x(x):
    if x % 2 == 0:
        return int(x / 2)
    return int(3 * x + 1)


print(muda_x(int(input("Informe um valor inteiro: "))))
