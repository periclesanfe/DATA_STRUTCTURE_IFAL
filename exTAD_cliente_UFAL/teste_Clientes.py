from TAD_Clientes import *

print("Teste do TAD Cliente")
print("NOMES")
qtd = int(input("Digite a quantidade de clientes: "))
agenda = CriarAgenda(qtd)

print('__________________________________________________________')
print('Agenda de Clientes')
for cliente in agenda:
    EscreveCliente(cliente)
    
print('__________________________________________________________') 
for cliente in agenda:
    if cliente.Fone[:2] == '82':
        EscreveCliente(cliente)
    else:
        print('Nenhum cliente encontrado')
    