# 6. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.


def verificadata(data):
    if not data.isdigit():
        return "Algum digito não é numero"
    if len(data) != 8:
        return "Data inválida"
    if 1 <= int(data[:2]) <= 31:
        if 1 <= int(data[2:4]) <= 12:
            return f"A data {data[:2]}/{data[2:4]}/{data[4:]} é válida"
        return "Mês inválido"
    return "Dia Inválido"


data = input("Digite a data no formato dd/mm/aaaa: ")
print(verificadata(data))
