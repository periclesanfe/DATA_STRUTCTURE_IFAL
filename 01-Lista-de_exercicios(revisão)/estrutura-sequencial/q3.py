# Faça um programa que pergunte quando você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário por mês.

valor = float(input('Quanto você ganha por hora? '))
horas = int(input('Quantas horas você trabalha por mês? '))
print('Você ganha R$'+str(valor*horas)+' por mês')