# Desenvolva um método/função recursiva para remover todos os elementos de uma pilha.
from pilha import PilhaArray

p = PilhaArray()
p.push(1)
p.push(2)
p.push(3)
print()

def remove_tudo(p):
    if not p:
        return
    p.pop()
    remove_tudo(p)

remove_tudo(p)
print(p)
