from pilha_vazia import PilhaException

class PilhaArray:
    def __init__(self, MAX=None):
        self.maximo = MAX if MAX is not None else float('inf')
        self._pilha = []
    
    def __len__(self):
        return len(self._pilha)

    def size(self):
        return self.__len__()

    def is_empty(self):
        return len(self._pilha) == 0

    def push(self, e):
        if self.is_full():
            raise PilhaException('A pilha está cheia')
        self._pilha.append(e)
    
    def top(self):
        if self.is_empty():
            raise PilhaException('A pilha está vazia')
        return self._pilha[-1]
    
    def pop(self):
        if self.is_empty():
            raise PilhaException('A pilha está vazia')
        return self._pilha.pop()
    
    def is_full(self):
        return self.size == self.maximo