# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.

while True:
    num = int(input("Digite um número entre zero e dez: "))
    if 0 <= num <= 10:
        break
    print(f"O número {num} é inválido. ", end="")
print(f"O número {num} é válido")
