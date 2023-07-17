# 3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
# ocorre 2 vezes em "estrutura"


def contador(palavra, letra):
    if len(palavra) == 0:
        return 0
    elif palavra[0] == letra:
        return 1 + contador(palavra[1:], letra)
    return contador(palavra[1:], letra)


palavra = input("Informe a palavra: ").lower()
letra = input("informe a letra: ").lower()

ocorrencias = contador(palavra, letra)

print(f"A letra {letra} apareceu {ocorrencias}x em {palavra}")
