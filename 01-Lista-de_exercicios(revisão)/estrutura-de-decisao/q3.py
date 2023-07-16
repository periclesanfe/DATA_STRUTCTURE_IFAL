# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = {
    1:"Domingo",
    2:"Segunda",
    3:"Terça",
    4:"Quarta",
    5:"Quinta",
    6:"Sexta",
    7:"Sabado"
}

dia = int(input('Digite o numero e descubra o dia: '))
for valor in semana:
    if dia == valor:
        print(semana[dia])
