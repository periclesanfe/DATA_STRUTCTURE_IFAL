from fila import FilaArray

f = FilaArray()
f.enqueue(5)
f.enqueue(3)
f.dequeue()
f.enqueue(2)
f.enqueue(8)
f.dequeue()
f.dequeue()
f.enqueue(9)
f.enqueue(1)
f.dequeue()
f.enqueue(7)
f.enqueue(6)
f.dequeue()
f.dequeue()
f.enqueue(4)
f.dequeue()
f.dequeue()
f.show()

# 5