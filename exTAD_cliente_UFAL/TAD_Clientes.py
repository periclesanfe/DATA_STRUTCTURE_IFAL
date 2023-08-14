class Cliente:
    def __init__(self):
        self.Nome = " "
        self.Fone = " "
    
def novoCliente():
    cad = Cliente()
    cad.Nome = input("Digite o nome do cliente: ")
    cad.Fone = input("Digite o telefone do cliente: ")
    return cad

def EscreveCliente(cad):
    print("Nome: ", cad.Nome)
    print("Telefone: ", cad.Fone,'\n')
    
def CriarAgenda(qtd):
    agenda = [Cliente()] * qtd
    for i in range (qtd):
        agenda[i] = novoCliente()
    return agenda