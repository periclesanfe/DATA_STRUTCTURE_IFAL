# Qual os valores retornados durante a seguinte série de operações em uma pilha, quando executadas em uma pilha 'p' inicialmente vazia?
# p.push(5), p.push(3), p.pop(), p.push(2), p.push(8), p.pop(), p.pop(), p.push(9), p.push(1), p.pop(),
# p.push(7), p.push(6), p.pop(), p.pop(), p.push(4), p.pop(), p.pop().

lista = []
lista.append(5)
lista.append(3)
lista.pop()
lista.append(2)
lista.append(8)
lista.pop()
lista.pop()
lista.append(9)
lista.append(1)
lista.pop()
lista.append(7)
lista.append(6)
lista.pop()
lista.pop()
lista.append(4)
lista.pop()
lista.pop()
print(lista)
