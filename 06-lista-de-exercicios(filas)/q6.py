class FilaException(Exception):
    pass

def enqueue(self, e):
        if self._tamanho == len(self._dados):
            raise FilaException('A Fila está Cheia')
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1