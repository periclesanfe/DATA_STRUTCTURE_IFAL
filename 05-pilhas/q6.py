# Crie uma função que copia todos os elementos de pilha p para outra pilha q, de forma que os elementos mantenham a
# mesma ordem, ou seja, o elemento no topo da pilha p permanecerá no topo da pilha q.

from pilha import PilhaArray

p = PilhaArray()
p.push(1)
p.push(2)
p.push(3)
q = PilhaArray()

def copia_pilha(p,q):
    if p.is_empty():
        return q
    else:
        q.push(p.top())
        return copia_pilha(p.pop(),q)   

copia_pilha(p,q)
print(q)
