# Faça um programa que peça a temperatura em graus Farenheit
# Transforme e mostre a temperatura em graus Celcius.
# C = (5 * (F-32) / 9)

def trans_celcius(f):
    return 5*(f-32)/9

print('A temperatura é : {:.2f}ºC'.format(trans_celcius(float(input('Informe a temperatura Fº: ')))))