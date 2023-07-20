# Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da
# mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
# papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

import string


# retorna se a palavra é palindroma
# dica: separa primeira e ultima letra e chama inverter novamente com as letras que restaram, se 1 ou 0 return True
def palindroma(palavra):
    palavra = semespacos(palavra)
    palavra = semespeciais(palavra)
    return inverte(palavra) == palavra


# inverte a palavra
def inverte(palavra):
    if len(palavra) == 0:
        return ""
    else:
        return inverte(palavra[1:]) + palavra[0]


# retira acentos
def semacentos(palavra):
    acentos = {
        "á": "a",
        "à": "a",
        "â": "a",
        "ã": "a",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ó": "o",
        "ò": "o",
        "ô": "o",
        "õ": "o",
        "í": "i",
        "ì": "i",
        "ú": "u",
        "ù": "u",
        "ç": "c",
    }

    for i in palavra:
        if i in acentos:
            pass


# caracteres especiais
def semespeciais(palavra):
    for i in palavra:
        if i in string.punctuation:
            i = ""
    return palavra


# retirar espaços
def semespacos(palavra):
    return palavra.replace(" ", "")


# TESTES
print(palindroma("ana"))
print(palindroma("E até o papa poeta é"))
print(palindroma("p"))
print(palindroma(""))
print(palindroma("p p p"))
print(semespeciais("E! até o*$#@ papa poeta é!"))
