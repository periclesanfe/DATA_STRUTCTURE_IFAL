# 5. Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.


def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return "É bissexto"
            return "Não é Bissexto"
        return "É bissexto"
    return "Não é bissexto"


print(bissexto(int(input("Informe o ano: "))))
