# 5. Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
for i in range(0, 5):
    lista.append(int(input("Informe um numero: ")))
lista.sort()
soma = sum(lista)
print(f"O a soma é {soma}")
print(f"A média é {soma/5}")
