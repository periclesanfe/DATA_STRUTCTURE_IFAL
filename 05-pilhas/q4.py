# Desenvolva uma função que inverte uma lista de elementos colocando-os todos em uma pilha, e colocando-os novamente
# na lista de forma invertida.

from pilha import PilhaArray

p = [1,2,3,4,5,6,7,8,9,10]

def inverte_lista(p):
    pilha = PilhaArray()
    for i in range(len(p) -1, -1, -1):
        pilha.push(p[i])
    return pilha
pilha = inverte_lista(p)
print(pilha)
