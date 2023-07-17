# 6. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 5.

saida = []
for i in range(1, 6):
    if i % 2 != 0:
        saida.append(str(i))

imprimir = ",".join(saida)
print(imprimir)
