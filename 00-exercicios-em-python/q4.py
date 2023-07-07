# Imprima uma tabela de multiplos de um numero
# A quantidade de numeros multiplos que vai ser impresso é a mesma do numero
# Exemplo: 3
# 1
# 2 4
# 3 6 9

n = int(input("Digite um numero: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
