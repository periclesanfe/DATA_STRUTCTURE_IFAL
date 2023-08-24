class FilaVazia(Exception):
    pass

class FilaArray:
    CAPACIDADE_PADRAO = 5
    
    def __init__(self):
        self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0
        
    def __len__(self):
        return self._tamanho
    
    def is_empty(self):
        return self._tamanho == 0
    
    def first(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        return self._dados[self._inicio]
    
    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) %len(self._dados)
        self._tamanho -= 1
        if 0 < self._tamanho < len(self._dados) // 4:
            self._aumenta_tamanho(len(self._dados) // 2)
        return result
    
    def enqueue(self, e):
        if self._tamanho == len(self._dados):
            self._aumenta_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1
        
    def _aumenta_tamanho(self, novo_tamanho):
        dados_antigos = self._dados 
        self._dados = [None] * novo_tamanho 
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao] 
            posicao = (1 + posicao) %len(dados_antigos) 
        self._inicio = 0
        
    def show(self):
        print(self)
        
    def __str__(self):
        posicao = self._inicio
        result = "["
        for k in range(self._tamanho):
            result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
        return result