from random import randint

lista_contas = []

class Conta:
    def __init__(self, nome_correntista, saldo):
        self._saldo = saldo
        self.numero_conta = randint(1000, 9999)
        self.nome_correntista = nome_correntista
        lista_contas.append(self.numero_conta)

        
    