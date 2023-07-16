# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um

# triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados
# for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def tipo_triangulo(lista):
    if (int(lista[0]) + int(lista[1])) > int(lista[2]):
        if lista[0] == lista[1] == lista[2]:
            return "Esse é um triangulo Equilátero"
        if lista[0]==lista[1] or lista[0]==lista[2] or lista[1]==lista[2]:
            return "Esse é um triangulo Isóceles"
        return "Esse é um triangulo Escaleno"
    else:
        return "A soma de dois quaisquer lados não é maior que um terceiro lado, Não pode ser um triangulo."


lista = []
for i in range(0, 3):
    lista.append(float(input(f"Informe o {i+1}º lado ")))
lista = sorted(lista)
print(tipo_triangulo(lista))
