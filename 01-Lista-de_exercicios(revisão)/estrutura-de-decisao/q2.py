# Faça um programa que leia três números e  mostre o maior e o menor deles.

lista = []
maior = 0
menor = 0
for i in range(0, 3):
    lista.append(float(input("Digite um número: ")))
lista = sorted(lista)
print(f"O maior número é {lista[-1]} e o menor é {lista[0]}")
        