# Supondo que a população de um país A seja da ordem de 80000 habitantes com
# uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
# e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
ano = 0
A = 80000.0
B = 200000.0
while True:
    ano += 1
    A = A * 1.03
    B = B * 1.015
    if A > B:
        break
print(
    "Foram necessários {} anos para o país A ultrapassar a população do país B, estando atualmente com {:.2f} e {:.2f} habitantes respectivamente.".format(
        ano, A, B
    ),
)
